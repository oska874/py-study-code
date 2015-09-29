import tftpy

server = tftpy.TftpServer('d:/vagrant/cagsdk')
server.listen('0.0.0.0', 69)