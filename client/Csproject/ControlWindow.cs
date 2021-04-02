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
            this.InitChart();
            CheckForIllegalCrossThreadCalls = false;
            this.toolStripComboBox1.Items.AddRange(SerialPort.GetPortNames());
            this.toolStripComboBox1.SelectedIndex = this.toolStripComboBox1.Items.Count - 1;
            this.toolStripButton1.Enabled = true;
        
            this.InitListener();
            this.InitialSerialPort();
 
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

       
    }
}
