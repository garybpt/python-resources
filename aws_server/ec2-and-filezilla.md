Original source By Mustafa Gonen (06/07/2022) - https://www.devopsmania.com/how-to-connect-an-aws-ec2-instance-with-filezilla-and-do-sftp/

# How to connect an AWS EC2 instance with FileZilla and do SFTP?

**Intro**

EC2 is one of the essential services of Amazon Web Services (AWS), providing highly available and scalable compute capacity. Amazon gives you nearly unlimited virtual machines to run your applications. So you frequently need to transfer files to that remote machines. For example, you move files to an EC2 instance when updating your applications. This article will teach you how to connect an AWS EC2 instance with Filezilla and do SFTP.

There are many alternative ways to perform the file transfer. But we are only going to talk about FTP and SFTP.

**What is FTP?**

FTP stands for File Transfer Protocol and this is a standard protocol that is used to transfer files between computers and servers over a network, such as the Internet. In other words, FTP is the language that computers use to transfer files over a TCP/IP network. For example, if someone anywhere in the world wanted to make their files available for other people to download, all they would have to do is simply upload their files to the FTP server. And then other people from anywhere in the world can simply connect to that FTP server and download the files using the FTP protocol.

**What is SFTP?**

The main drawback of FTP is that it’s not a secure protocol. So the data is not encrypted while transferring. Sending it as clear text can cause security concerns. Then SFTP comes in. It stands for Secure File Transfer Protocol. SFTP adds a layer of security. The secure FTP data is encrypted using a secure shell (SSH) during data transfer. So no information is sent in clear text; it’s all encrypted. And Secure FTP authenticates both the user and the server, using port 22.

**FileZilla Client with SFTP**

There are a couple of ways to transfer files using FTP. You can use your standard internet browser or use an FTP client. But, FTP clients provide a graphical user interface and a better overall experience than using a web browser. The most popular free FTP client is FileZilla, which you can download for free. FileZilla is an open-source, cross-platform FTP application, consisting of FileZilla Client and FileZilla Server. Clients are available for Windows, Linux, and macOS, servers are available for Windows only. Both server and client support FTP, while the client can, in addition, connect to SFTP servers.

**Steps To Create an Amazon EC2 Instance**

1. Visit aws.amazon.com and login in with your account.
2. Navigate to AWS console select EC2 service.
3. Click on Launch instances.
4. Choose Amazon Linux 2 AMI (Free tier eligible). Click Select.
5. Choose instance-type t2.micro and click on Next Configure details.
6. Keep defaults and follow the path Add Storage >> Add Tags >> Configure Security Groups.
7. Create a new security group; name it. Allow SSH port 22. Choose the “My IP option” as Source to specify only your IP address and restrict access to your instance. It is not a best practice to open SSH port 22 to whole world. This “My IP” is where you are going to upload your documents using SFTP
8. Click on Review and Launch then Launch.
9. Choose a key pair or create one if not having any. And, we are good to launch the EC2 instance.

Now, we have an EC2 instance created. Let’s try to upload the files to the server using Filezilla.

**Steps to connect an AWS EC2 Instance with Filezilla and do SFTP**

1. Download and install the FileZilla client suitable for your operating system.

2. Open FileZilla and follow the path Edit (Preferences) > Settings > Connection > SFTP, Click “Add key file”

3. Browse to the location of your example_key.pem file you use to connect your EC2 instance and select it.

4. If the new file is shown in the list of Keyfiles, then click it and Ok and continue to the next step. 

5. File > Site Manager Add a New site with the following parameters:

```–Protocol: SFTP – SSH File Transfer Protocol

–Host: The public DNS name of your EC2 instance, or the public IP address of the server.

–Port: 22

–Logon Type: Normal

–User: For Amazon Linux, the default user name is ec2-user. For others check the docs.
```

6. Press Connect Button

!!! If the saving of passwords has been disabled, you will be prompted that the logon type will be changed to ‘Ask for password’. Say ‘OK’ and when connecting, at the password prompt push ‘OK’ without entering a password to proceed past the dialog!!!

NOTE: FileZilla automatically figures out which key to use. You do not need to specify the key after importing it as described above.

7. Vois là! Drag and drop your files/folders freely between local machine and EC2 instance you created, via the UI on Filezilla.

8. Do not forget to terminate the EC2 instance to avoid extra charge!

Conclusion
In this article, you learned file transfer methods, the difference between FTP and SFTP, and how to connect an AWS EC2 instance with FileZilla and do SFTP. If you have any contributions or questions, do not hesitate to contact!