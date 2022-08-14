//说明：本程序用于接收UDP数据包，远程遥控机器人运动
#include <stdio.h>
#include <iostream>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <errno.h>
#include <string.h>
#include <ros/ros.h>
//#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

char blocks[100][901];//要发送的数据包

#define inputImageHeight 480
#define inputImageWidth 640
#define rawImageHeight 150
#define rawImageWidth 200
#define rawBlockNum 10


class UPD_Receiver
{
public:
	UPD_Receiver(int monitorPort)
	{
		OK = 0;
		memset(&addr_client,sizeof(addr_client),0);
		sock_fd = socket(AF_INET, SOCK_DGRAM, 0);//创建UDP套接字
		if(sock_fd < 0)
		{
			printf("socket ERROR\n");
			return;
		}
		struct sockaddr_in addr_serv;
		memset(&addr_serv, 0, sizeof(struct sockaddr_in));//每个字节都用0填充
		addr_serv.sin_family = AF_INET;//使用IPV4地址
		addr_serv.sin_port = htons(monitorPort);//监听的端口
		addr_serv.sin_addr.s_addr = htonl(INADDR_ANY);//自动获取IP地址，INADDR_ANY表示接收所有网卡的数据
		if(bind(sock_fd, (struct sockaddr *)&addr_serv, sizeof(addr_serv)) < 0)//绑定socket
		{
			perror("bind error:");
			return;
		}
		OK = 1;//初始化成功
	}
	int receive(char* recv_buf, int bufLength)//监听目标端口的消息
	{
		int len;
		return recvfrom(sock_fd, recv_buf, bufLength, MSG_DONTWAIT, (struct sockaddr *)&addr_client, (socklen_t *)&len);
	}
	int send(char* send_buf, int bufLength)//向远程端口回传数据
	{
		return sendto(sock_fd, send_buf, bufLength, 0, (struct sockaddr *)&addr_client, len2);
	}
	int len2 = sizeof(addr_client);
	int OK;//初始化成功标志
	int sock_fd;//UDP套接字
	struct sockaddr_in addr_client;
protected:
private:
};

int main(int argc, char** argv)
{
	printf("internet init\r\n");
	UPD_Receiver receiver(9001);
	if(receiver.OK != 1)
	{
		printf("init error\r\n");
		return 0;
	}
	printf("camera init\r\n");
	Mat frame;//从相机接收的图像
	ros::init(argc, argv, "aim_XR");
	ros::NodeHandle my_node;
	VideoCapture cap(0);
	if(!cap.isOpened())//摄像头打开错误
	{
		cout << "No Camera!" << endl;
		return -1;
	}
	cap.set(CAP_PROP_FOURCC,CV_FOURCC('M','J','P','G'));//MJPEG方式传输图像可大幅提高帧率（6Hz->30Hz）
	cap.set(CAP_PROP_FRAME_WIDTH,inputImageWidth);
	cap.set(CAP_PROP_FRAME_HEIGHT,inputImageHeight);
	char recvBuf[1050];
	int recvNum = 0;
	/*
	while(1)
	{
		recvNum = receiver.receive(recvBuf, 1000);
		if(recvNum > 0)
		{
			recvNum = receiver.send(recvBuf, recvNum);
			if(recvNum <= 0) perror("err");
		}
	}
	*/
	while(receiver.receive(recvBuf, 1000) <= 0)
	{
		if(errno != EAGAIN) perror("err");
		printf("wait for connection\r\n");
		usleep(1000000);//等待遥控器建立链接
	}
	printf("connected\r\n");
	ros::Time timeNow = ros::Time::now();
	ros::Time StartTime = ros::Time::now();
	ros::Time FinishTime = ros::Time::now();
	while(ros::ok())
	{
		cout << "fps:\t" << 1.0/(ros::Time::now() - timeNow).toSec() << "\t\t\t" << (FinishTime - StartTime).toSec() / (ros::Time::now() - StartTime).toSec() <<endl;//帧率显示
		StartTime = ros::Time::now();
		timeNow = ros::Time::now();
		cap >> frame;
//		recvNum = receiver.receive(recvBuf, 1000);//更新遥控器状态（IP地址及端口号）
		//开始发送数据
		for (int i = 0; i < rawImageHeight; i++)//像素在发送图像中的位置Y
		{
			uchar *p = frame.ptr<uchar>(15 + i * 3);
			for (int j = 0; j < rawImageWidth; j++)//像素在发送图像中的位置X
			{
				int blockID = i % 15 + j % 20;
				int blocksFillNum = 1 + (j / 20 + i / 15 * 10) * 3;
				if(blockID > 100 || blockID < 0 || blocksFillNum >= 900 || blocksFillNum <= 1)
					printf("error!%d\t%d\n",blockID,blocksFillNum);
				blocks[blockID][blocksFillNum] = p[(20 + j * 3) * 3 + 0];//B
				blocks[blockID][blocksFillNum+1] = p[(20 + j * 3) * 3 + 1];//G
				blocks[blockID][blocksFillNum+2] = p[(20 + j * 3) * 3 + 2];//R
			}
		}
		//printf("\n");
		for(int i = 0; i < 100; i++)
		{
			blocks[i][0] = i;//添加消息ID
			//printf("%d,",blocks[i][0]);
			recvNum = receiver.send(blocks[i], 901);
			if(recvNum <= 0)//发送失败
			{
				printf("errno=%d\n",errno);
				perror("send error");
			}
			usleep(150);
		}
		//printf("\n");
		usleep(20000);
		FinishTime = ros::Time::now();
	}
	return 0;
}











