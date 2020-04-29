import urllib.request as req
import gzip, os, os.path

savepath = "./mnist"
baseurl="http://yann.lecun.com/exdb/mnist"
files = [
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz" ]



#압축해제    
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz","")
    print("gzip:",f)
    with gzip.open(gz_file,"rb") as fp:
        body = fp.read()
        with open(raw_file,"wb") as w:
            w.write(body)

print("ok")            
