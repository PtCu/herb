using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace Csproject
{
    public class ClientSocket
    {
        string host;
        int port;
        Socket socket;
        public ClientSocket(string h, int p)
        {
            host = h;
            port = p;
            // 将将IP地址字符串转换为IPAddress对象
            IPAddress ip = IPAddress.Parse(host);
            // 创建终结点EndPoint
            IPEndPoint ipe = new IPEndPoint(ip, port);
            //============================================================================//
            // 2、创建socket连接客户端      
            // 创建Socket并连接到服务器
            socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            // 连接到服务器
            socket.Connect(ipe);
        }
        public void Send(string msg)
        {
            // 将字符串消息转为数组
            byte[] bytes = Encoding.ASCII.GetBytes(msg);
            //发送消息给客户端
            socket.Send(bytes, bytes.Length, 0);
        }
        //开启监听线程
        public void start()
        {
            socket.Listen(0);
            while (true)
            {   
                    Socket remote = socket.Accept();
                    // 接收客户端消息
                    Receive(remote);
                    // 发送给客户端消息
                    Send(remote);
                

            }
        }
        public string Receive()
        {
            byte[] bytes = new byte[1024];
            //从客户端接收消息
            int len = socket.Receive(bytes, bytes.Length, 0);
            //将消息转为字符串
            string recvStr = Encoding.ASCII.GetString(bytes, 0, len);
            return recvStr;
        }

    }
}
