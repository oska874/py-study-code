# -*- coding: utf-8 -*- 
import zlib,urllib

fp = urllib.urlopen('http://126.com')    
# 访问的到的网址。  
data = fp.read()  
fp.close()  

#print(data)

com_obj1=zlib.compressobj()
decom_obj1=zlib.decompressobj()

chunk_size = 30
print("before compress : " + str(len(data)))

#原始数据分块  
str_chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range((len(data) + chunk_size) / chunk_size)]  
   
str_obj2 = ''  
for chunk in str_chunks:
	str_obj2 += com_obj1.compress(chunk)  
str_obj2 += com_obj1.flush()  
print ('分块压缩后： %d' % len(str_obj2))
   
#压缩数据分块解压  
str_chunks = [str_obj2[i * chunk_size:(i + 1) * chunk_size] for i in range((len(str_obj2) + chunk_size) / chunk_size)]  
str_obj2 = ''  
for chunk in str_chunks:
	str_obj2 += decom_obj1.decompress(chunk)  
str_obj2 += decom_obj1.flush()  
print ('分块解压后：%d '% len(str_obj2) )
