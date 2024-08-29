# coding:utf-8
import wx
from socket import socket,AF_INET,SOCK_STREAM
import threading

class Client(wx.Frame):
    
    def __init__(self, client_name):
        # 调用父类的初始化方法
        # None: 没有父级窗口
        # ID表示当前窗口的一个编号
        # pos，窗体的打开位置
        # size：窗体的大小，单位是像素，400宽，450高度
        wx.Frame.__init__(self,None,id=1001,title=client_name+'的客户端',pos=wx.DefaultPosition,size=(400,450))
        # 创建面板对象
        pl=wx.Panel(self)
        
        box=wx.BoxSizer(wx.VERTICAL)  # 垂直方向布局
        
        # 可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局
        
        # 创建两个按钮
        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        dis_conn_btn=wx.Button(pl,size=(200,40),label='断开')
        
        # 把两个按钮放到可伸缩的网格布局
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        
        # (可伸缩的网格布局)添加到box中
        box.Add(fgz1,1,wx.ALIGN_CENTRE)
        
        # 创建只读文本框，显示聊天内容
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTRE)
        
        # 创建聊天内容的文本框
        self.chat_text=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.chat_text,1,wx.ALIGN_CENTRE)
        
        # 可伸缩的网格布局
        fgz2=wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局
                
        # 创建两个按钮
        reset_btn=wx.Button(pl,size=(200,40),label='重置')
        send_btn=wx.Button(pl,size=(200,40),label='发送')
        
        # 把两个按钮放到可伸缩的网格布局
        fgz2.Add(reset_btn,1,wx.TOP|wx.LEFT)
        fgz2.Add(send_btn,1,wx.TOP|wx.RIGHT)
        
        # (可伸缩的网格布局)添加到box中
        box.Add(fgz2,1,wx.ALIGN_CENTRE)
        
        # 将盒子放到面板中
        
        pl.SetSizer(box)
        
        '''---------------------------以上代码是客户端界面的绘制-------------------------------------'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)
        # 实例属性的设置
        self.client_name=client_name
        self.isConnected=False # 存储客户端连接服务器的状态，默认为False，没连
        self.client_socket=None # set client object socket as None
        
    def connect_to_server(self,event):
        print(f'client {self.client_name} connected to server successful')
        # if client didn't connect to server, then start connection
        if not self.isConnected: # equal self.isConnected==False
            # TCP Programming steps
            server_host_port=('127.0.0.1',8888)
            # create socket object
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            # 发送连接请求
            self.client_socket.connect(server_host_port)
            # 只要连接成功，发送一条数据
            self.client_socket.send(self.client_name.encode('utf-8'))
            # 启动一个线程，客户端的线程与服务器端的线程进行会话
            client_thread=threading.Thread(target=self.recv_data)
            # 设置成守护线程，窗体关掉，子线程也结束了
            client_thread.daemon=True
            # 修改一下连接状态
            self.isConnected=True
            # 启动线程
            client_thread.start()
            
            
            
            
            
    def recv_data(self):
        # 如果是连接
        while self.isConnected:
            # 接收来自服务器的数据
            data=self.client_socket.recv(1024).decode('utf-8')
            
            #显示到只读文本框中
            self.show_text.AppendText('-'*40+'\n'+data+'\n')
        
        

if __name__ == '__main__':
    # 初始化App()
    app=wx.App()
    
    # 创建自己的客户端界面对象
    client=Client('PythonZyx')
    client.Show()  # 可以改成  Client('PythonZyx').show()
    
    
    # 循环刷新显示
    app.MainLoop()
    
    
        
        
        






        
        
        