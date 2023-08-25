clear
rosshutdown
rosinit
testserver = rossvcserver("/test","experiments/example",@serviceCallback,"DataFormat","struct");
testserver.NewRequestFcn = @serviceCallback;
while true
    pause(0.1)
end

function response = serviceCallback(src,reqMsg,defaultRespMsg)
    response = defaultRespMsg;
    response.XUndis = 10;
end