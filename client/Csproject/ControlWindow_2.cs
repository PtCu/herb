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
    //这个文件实现与arduino的交互
    public partial class ControlWindow : Form
    {
        void port_DataSend(String s)
        {
            try
            {

                if (port != null && port.IsOpen)
                {
                    port.Write(s);
                }

            }
            catch (Exception ex)
            {
                //捕获可能发生的异常并进行处理

                //捕获到异常，创建一个新的对象，之前的不可以再用

                port = new System.IO.Ports.SerialPort();
                MessageBox.Show("写串口数据发生错误：" + ex.Message, "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);

            }



        }
        void port_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            try
            {
                if (port != null && port.BytesToRead > 0)
                {
                    string str = port.ReadLine();
                    string[] sArray = str.Split('|');
                    if (sArray.Length != 4) return;
                    temperature_cur = sArray[0];
                    humidity_cur = sArray[1];
                    light_cur = sArray[2];
                    press_cur = sArray[3];
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
                series1.Points.AddXY(time, temperature_cur);
                series12.Points.AddXY(time, temperature_expected);
                chart1.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
                series2.Points.AddXY(time, humidity_cur);
                series22.Points.AddXY(time, humidity_expected);
                chart2.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
                series3.Points.AddXY(time, light_cur);
                series32.Points.AddXY(time, light_expected);
                chart3.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
                series4.Points.AddXY(time, press_cur);

                series42.Points.AddXY(time, press_expected);
                chart4.ChartAreas[0].AxisX.ScaleView.Position = series1.Points.Count - 9;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "读取串口错误，提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}
