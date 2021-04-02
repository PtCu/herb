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
    //这个文件实现公有函数
    public partial class ControlWindow : Form
    {
        //更新数据
        private void UpdateSet(string data)
        {
            string[] sArray = data.Split('|');
            if (sArray.Length != 4) return;
            string toShow = "设置：";
            if (System.Double.TryParse(sArray[0], out temperature_expected))
                toShow += "温度: " + temperature_expected;
            if (System.Double.TryParse(sArray[1], out humidity_expected))
                toShow += "湿度" + humidity_expected;
            if (System.Double.TryParse(sArray[2], out light_expected))
                toShow += "光强" + light_expected;
            if (System.Double.TryParse(sArray[3], out press_expected))
                toShow += "压强" + press_expected;
            textBox1.AppendText(toShow+"\r\n");
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
        var objects = new { id = 1, w = temperature_cur, s = humidity_cur, g = light_cur, y = press_cur, img = strbaser64 };
        string strings = JsonConvert.SerializeObject(objects);
        return strings;
    }

}
}
