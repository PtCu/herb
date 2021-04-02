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
    //这个文件实现事件函数
    public partial class ControlWindow : Form
    {
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

        //timer1到时，发送数据
        private void timer1_Tick(object sender, EventArgs e)
        {
            string data = getData();
            SendToServer(data);

        }

        //timer2到时，比较设定温度并调节
        private void timer2_Tick(object sender, EventArgs e)
        {
            

        }

        //提交本地设定（设定温度等）
        private void toolStripButton1_Click(object sender, EventArgs e)
        {

            try
            {
                string a, b, c, d;
                a = toolStripTextBox1.Text;
                b = toolStripTextBox2.Text;
                c = toolStripTextBox3.Text;
                d = toolStripTextBox4.Text;

                UpdateSet(a + "|" + b + "|" + c + "|" + d);

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        //开启、关闭摄像
        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            try
            {
                if (!videoSourcePlayer1.IsRunning)
                    videoSourcePlayer1.Start();
                else videoSourcePlayer1.Stop();
            }
            catch (Exception ex)
            {
                MessageBox.Show("捕获图像失败！" + ex.Message, "提示");
            }
        }
    }
}
