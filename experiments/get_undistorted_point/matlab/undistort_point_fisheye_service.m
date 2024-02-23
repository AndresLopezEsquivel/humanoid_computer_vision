% function undistort_point_service
% Remember to:
% rosgenmsg from the dir where you have all your packages
% clear
% rosshutdown
% rosinit

testserver = rossvcserver("srv/UndistortPoint","vision_msgs_and_srv/UndistortPoint",@serviceCallback, "DataFormat","struct");
% testserver.NewRequestFcn = @serviceCallback;
while true
    pause(0.1)
end

% function response = serviceCallback(src,reqMsg,defaultRespMsg)
%     class(defaultRespMsg)
%     properties(defaultRespMsg)
%     response = defaultRespMsg;
%     response.XUndis = 10;
% end

function response = serviceCallback(src,reqMsg,defaultRespMsg)
    % == CAMERA PARAMETERS ==
    mappingCoefficients = [5.420700282657709e+02 -6.365578727668607e-04 -1.845143184037665e-07 -1.434269892513010e-10];
    distortionCenter = [6.968767830094720e+02 3.466703380573117e+02];
    imageSize = [720 1280];
    intrinsics = fisheyeIntrinsics(mappingCoefficients,imageSize,distortionCenter);
    % class(defaultRespMsg)
    % properties(defaultRespMsg)
    % properties(reqMsg)
    x_dist = reqMsg.XDist;
    y_dist = reqMsg.YDist;
    dist_points = [x_dist, y_dist];
    udis_points = undistortFisheyePoints(dist_points, intrinsics);
    response = defaultRespMsg;
    class(response)
    % response = ros.msggen.experiments.exampleResponse;
    % class(defaultRespMsg)
    response.XUndis = udis_points(1);
    response.YUndis = udis_points(2);
end

% end