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
    //这个文件实现与server的交互
    //server的温度等的数据类型为var
    public partial class ControlWindow : Form
    {



        String Request(HttpListenerRequest request)
        {
            string temp = "";
             if (request.HttpMethod.ToLower().Equals("post"))
             {
                //POST请求处理
                try
                {

                    var responseString = new StreamReader(request.InputStream, Encoding.GetEncoding("utf-8")).ReadToEnd();
                    RootObject obj = JsonConvert.DeserializeObject<RootObject>(responseString.ToString());
                    UpdateSet(obj.temperature + '|' + obj.humidity + '|' + obj.light + '|' + obj.press);

                    //成功则返回"Accept"
                    temp = "Accept";
                }
                catch (Exception ex)
                {
                    temp = "Error";
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
        static void Response(HttpListenerResponse response, string responsestring, string contenttype = "application/json;charset=UTF-8")
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


        // 接收服务端发来信息的方法
        private void GetContextCallBack(IAsyncResult ar)
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


        //发送字符信息到服务端。
        private void SendToServer(string sendMsg)
        {
            string _url = "http://" + host_url + ":" + host_port + "/monitor/";
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
    }
}
