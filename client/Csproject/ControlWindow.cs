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
    //这个文件实现初始化
    public partial class ControlWindow : Form
    {
        private SerialPort port = null;
        string temperature_cur = ""; //当前值
        string humidity_cur = "";
        string light_cur = "";
        string press_cur = "";
        double temperature_expected = 100; //期望值
        double humidity_expected = 100;
        double light_expected = 100;
        double press_expected = 100;
        string host_url = "127.0.0.1";  //服务器ip
        string host_port = "8080";      //服务器端口
        string listen_port = "8000"; //本地监听端口
        readonly double temperature_thre=1; //温度阈值，当当前温度和设定温度之差超过此值时触发加热
        readonly double humidity_thre=1;
        readonly double light_thre=10;
        readonly double press_thre=10;
        FilterInfoCollection videoDevices;
        VideoCaptureDevice videoSource;

        //创建 1个客户端套接字 和1个负责监听服务端请求的线程  
        //Thread threadclient = null;
        HttpListener _listener;
        // Socket socketclient = null;
        private struct RootObject
        {
            public string temperature { get; set; }
            public string humidity { get; set; }
            public string light { get; set; }
            public string press { get; set; }
            //public string img { get; set; }
        }
        public ControlWindow()
        {
           
            InitializeComponent();
            CheckForIllegalCrossThreadCalls = false;
            this.toolStripComboBox1.Items.AddRange(SerialPort.GetPortNames());
            this.toolStripComboBox1.SelectedIndex = this.toolStripComboBox1.Items.Count - 1;
            this.toolStripButton1.Enabled = true;
            this.InitChart();
            this.InitialSerialPort();
            this.InitListener();

        }

        //如果初始化时对窗口进行写操作会报错
        //初始化chart
        private void InitChart()
        {
            try
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
            catch (Exception ex)
            {
                MessageBox.Show("初始化窗口发生错误：" + ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }


        }
        //初始化socket
        private void InitListener()
        {
            try
            {
                _listener = new HttpListener();
                _listener.Prefixes.Add("http://127.0.0.1:" + listen_port + "/");
                _listener.Start();
                _listener.BeginGetContext(new AsyncCallback(GetContextCallBack), _listener);

            }
            catch (Exception ex)
            {
                MessageBox.Show("初始化窗口发生错误：" + ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
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

       
    }
}
