import tftpy

server = tftpy.TftpServer('./')
server.listen('0.0.0.0', 69)
