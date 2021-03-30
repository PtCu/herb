using AForge.Video.DirectShow;
using Newtonsoft.Json;
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.IO.Ports;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;


namespace Csproject
{

    public partial class Form1 : Form
    {
        private SerialPort port = null;
        string w_value = "";
        string s_value = "";
        string g_value = "";
        string y_value = "";
        string w_set = "100";
        string s_set = "100";
        string g_set = "100";
        string y_set = "100";
        FilterInfoCollection videoDevices;
        VideoCaptureDevice videoSource;
        //创建 1个客户端套接字 和1个负责监听服务端请求的线程  
        Thread threadclient = null;
        HttpListener _listener;
        // Socket socketclient = null;
        private struct RootObject
        {
            public string w { get; set; }
            public string s { get; set; }
            public string g { get; set; }
            public string y { get; set; }
            //public string img { get; set; }
        }
        public Form1()
        {
            InitializeComponent();
            CheckForIllegalCrossThreadCalls = false;
            this.InitListener();
            this.toolStripComboBox1.Items.AddRange(SerialPort.GetPortNames());
            this.toolStripComboBox1.SelectedIndex = this.toolStripComboBox1.Items.Count - 1;
            this.toolStripButton1.Enabled = true;
            this.InitialSerialPort();
            this.InitChart();
        }



        //初始化socket
        private void InitListener()
        {
            _listener.Prefixes.Add("http://127.0.0.1:8080/");
            _listener.Start();
            _listener.BeginGetContext(new AsyncCallback(GetContextCallBack), _listener);

              }

        string Request(HttpListenerRequest request)
        {
            string temp = "welcome to linezero!";
            if (request.HttpMethod.ToLower().Equals("get"))
            {
                //GET请求处理

            }
            else if (request.HttpMethod.ToLower().Equals("post"))
            {

                //POST请求处理
                var responseString = new StreamReader(request.InputStream, Encoding.GetEncoding("utf-8")).ReadToEnd();
                RootObject objects = JsonConvert.DeserializeObject<RootObject>(responseString.ToString());
                if (w_set != objects.w || s_set != objects.s || g_set != objects.g ||
               y_set != Convert.ToString((int)(double.Parse(objects.y) * 1000)))
                {
                    w_set = objects.w; s_set = objects.s; g_set = objects.g;
                    y_set = Convert.ToString((int)(double.Parse(objects.y) * 1000));
                    UpdateSet(w_set + "|" + s_set + "|" + g_set + "|" + y_set);
                    textBox1.AppendText("set:" + w_set + ' ' + s_set + ' ' + g_set + ' ' + y_set + "\r\n");
                }

            }
            return temp;
        }


        /// <summary>
        /// 输出方法
        /// </summary>
        /// <param name="response">response对象</param>
        /// <param name="responseString">输出值</param>
        /// <param name="contenttype">输出类型默认为json</param>
        static void Response(HttpListenerResponse response, string responsestring, string contenttype = "application/json")
        {
            response.StatusCode = 200;
            response.ContentType = contenttype;
            response.ContentEncoding = Encoding.UTF8;
            byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responsestring);
            //对客户端输出相应信息.
            response.ContentLength64 = buffer.Length;
            System.IO.Stream output = response.OutputStream;
            output.Write(buffer, 0, buffer.Length);
            //关闭输出流，释放相应资源
            output.Close();
        }

        //发送字符信息到服务端的。
        private void SendToServer(string sendMsg)
        {
            string _url = "http://localhost:1900/monitor/";
            var request = (HttpWebRequest)WebRequest.Create(_url);
            request.Method = "POST";
            request.ContentType = "application/json;charset=UTF-8";
            byte[] byteData = Encoding.UTF8.GetBytes(sendMsg);
            int length = byteData.Length;
            request.ContentLength = length;
            Stream writer = request.GetRequestStream();
            writer.Write(byteData, 0, length);
            writer.Close();

        }
        // 接收服务端发来信息的方法
        private void GetContextCallBack(IAsyncResult ar)
        {
            try
            {
                _listener = ar.AsyncState as HttpListener;
                HttpListenerContext context = _listener.EndGetContext(ar);
                //再次监听请求
                _listener.BeginGetContext(new AsyncCallback(GetContextCallBack), _listener);
                //处理请求
                string a = Request(context.Request);
                //输出请求
                Response(context.Response, a);
            }
            catch { }

           
        }

        //初始化chart
        private void InitChart()
        {
            foreach (var item in tableLayoutPanel1.Controls)
            {
                if (item is Chart)
                {
                    Chart chart = item as Chart;
                    chart.ChartAreas[0].AxisX.LabelStyle.Format = "HH:mm";
                    chart.ChartAreas[0].AxisX.ScaleView.Size = 10;
                    chart.ChartAreas[0].AxisX.ScrollBar.Enabled = false;
                }
            }
        }

        //初始化串口
        private void InitialSerialPort()
        {
            try
            {
                string portName = this.toolStripComboBox1.SelectedItem.ToString();
                port = new SerialPort(portName, 9600);
                port.Encoding = Encoding.ASCII;
                port.DataReceived += port_DataReceived;
                port.Open();
            }
            catch (Exception ex)
            {
                MessageBox.Show("初始化串口发生错误：" + ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        //初始化摄像
        private void Form1_Load_1(object sender, EventArgs e)
        {
            videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            videoSource = new VideoCaptureDevice(videoDevices[0].MonikerString);//连接摄像头。
            videoSource.VideoResolution = videoSource.VideoCapabilities[0];
            videoSourcePlayer1.VideoSource = videoSource;
            videoSourcePlayer1.Start();
        }
        //关闭摄像
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            videoSourcePlayer1.Stop();
        }
        //定时器触发回调函数
        private void timer1_Tick(object sender, EventArgs e)
        {
            /*      if (port != null && port.IsOpen)
                  {
                      port.WriteLine(w_set + '|' + s_set + '|' + g_set + '|' + y_set);
                  }*/
            string data = getData();
            SendToServer(data);

        }
        private void UpdateSet(string data)
        {
            if (!port.IsOpen)
            {
                try
                {
                    port.Open();
                    port.Write(data);
                    port.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);

                }
            }
        }
        //提交本地设定（设定温度等）
        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            try
            {
                /*         double set_w = double.Parse(toolStripTextBox1.Text);
                         set_w = double.Parse(toolStripTextBox2.Text);
                         set_w = double.Parse(toolStripTextBox3.Text);
                         set_w = double.Parse(toolStripTextBox4.Text);*/
                w_set = toolStripTextBox1.Text;
                s_set = toolStripTextBox2.Text;
                g_set = toolStripTextBox3.Text;
                y_set = toolStripTextBox4.Text;

                UpdateSet(w_set + "|" + s_set + "|" + g_set + "|" + y_set);
                /*var objects = new { id = 1, w = w_set, s = s_set, g = g_set, y = (Convert.ToDouble(y_set) / 1000) };
                string strings = JsonConvert.SerializeObject(objects);
                //string _url = "http://localhost:8080/iotSystem/monitorc/";
                string _url = "http://localhost:1900/monitorc/";*/
                /*var request = (HttpWebRequest)WebRequest.Create(_url);
                request.Method = "POST";
                request.ContentType = "application/json;charset=UTF-8";
                byte[] byteData = Encoding.UTF8.GetBytes(strings);
                int length = byteData.Length;
                request.ContentLength = length;
                Stream writer = request.GetRequestStream();
                writer.Write(byteData, 0, length);
                writer.Close();
                var response = (HttpWebResponse)request.GetResponse();
                var responseString = new StreamReader(response.GetResponseStream(), Encoding.GetEncoding("utf-8")).ReadToEnd();
                RootObject objects2 = JsonConvert.DeserializeObject<RootObject>(responseString.ToString());

                w_set = objects2.w; s_set = objects2.s; g_set = objects2.g; y_set = Convert.ToString((int)(double.Parse(objects2.y) * 1000));
                textBox1.AppendText("set:" + w_set + ' ' + s_set + ' ' + g_set + ' ' + y_set + "\r\n");*/

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        //关闭摄像
        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            videoSourcePlayer1.Stop();
        }

        //捕捉图形
        private void toolStripButton3_Click(object sender, EventArgs e)
        {
            try
            {
                /*string fileImageName = "banlcer.jpg";
                string fileCapturePath = "2020test\\";
                if (!Directory.Exists(fileCapturePath))
                    Directory.CreateDirectory(fileCapturePath);*/
                //抓到图保存到指定路径
                /* string data = getData();
                 SendToServer(data);*/
            }
            catch (Exception ex)
            {
                MessageBox.Show("捕获图像失败！" + ex.Message, "提示");
            }
        }

        private string getData()
        {
            Image img = null;
            img = videoSourcePlayer1.GetCurrentVideoFrame();

            if (img == null)
            {
                img = new Bitmap("test.jpg");

            }
            MemoryStream ms = new MemoryStream();
            img.Save(ms, ImageFormat.Jpeg);
            byte[] bytes = ms.ToArray();
            ms.Close();
            //img.Save(fileCapturePath + fileImageName, ImageFormat.Jpeg);
            string strbaser64 = Convert.ToBase64String(bytes);
            //string imgStr = "data:image/jpg;base64," + strbaser64;
            var objects = new { id = 1, w = w_value, s = s_value, g = g_value, y = y_value, img = strbaser64 };
            string strings = JsonConvert.SerializeObject(objects);
            return strings;
        }
        void port_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {

            try
            {
                if (port != null && port.BytesToRead > 0)
                {
                    string str = port.ReadLine();
                    string[] sArray = str.Split('|');
                    w_value = sArray[0];
                    s_value = sArray[1];
                    g_value = sArray[2];
                    y_value = sArray[3];
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("读取串口数据发生错误：" + ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            try
            {
                Series series1 = chart1.Series[0];
                Series series12 = chart1.Series[1];
                Series series2 = chart2.Series[0];
                Series series22 = chart2.Series[1];
                Series series3 = chart3.Series[0];
                Series series32 = chart3.Series[1];
                Series series4 = chart4.Series[0];
                Series series42 = chart4.Series[1];
                DateTime time = DateTime.Now;
                series1.Points.AddXY(time, w_value);
                series12.Points.AddXY(time, w_set);
                chart1.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
                series2.Points.AddXY(time, s_value);
                series22.Points.AddXY(time, s_set);
                chart2.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
                series3.Points.AddXY(time, g_value);
                series32.Points.AddXY(time, g_set);
                chart3.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
                series4.Points.AddXY(time, y_value);

                series42.Points.AddXY(time, y_set);
                chart4.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "读取串口错误，提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
        /*        private void httpToServer(string strings)
                {
                    //string _url = "http://localhost:8080/iotSystem/monitor/";
                    string _url = "http://localhost:1900/monitor/";
                    var request = (HttpWebRequest)WebRequest.Create(_url);
                    request.Method = "POST";
                    request.ContentType = "application/json;charset=UTF-8";
                    byte[] byteData = Encoding.UTF8.GetBytes(strings);
                    int length = byteData.Length;
                    request.ContentLength = length;
                    Stream writer = request.GetRequestStream();
                    writer.Write(byteData, 0, length);
                    writer.Close();

                    var response = (HttpWebResponse)request.GetResponse();
                    var responseString = new StreamReader(response.GetResponseStream(), Encoding.GetEncoding("utf-8")).ReadToEnd();
                    RootObject objects2 = JsonConvert.DeserializeObject<RootObject>(responseString.ToString());
                    if (w_set != objects2.w || s_set != objects2.s || g_set != objects2.g ||
                        y_set != Convert.ToString((int)(double.Parse(objects2.y) * 1000)))
                    {
                        w_set = objects2.w; s_set = objects2.s; g_set = objects2.g;
                        y_set = Convert.ToString((int)(double.Parse(objects2.y) * 1000));
                        textBox1.AppendText("set:" + w_set + ' ' + s_set + ' ' + g_set + ' ' + y_set + "\r\n");
                    }


                }*/




    }
}
