function undistort_point_service
% Remember to:
% rosgenmsg from the dir where you have all your packages
% clear
% rosshutdown
% rosinit

testserver = rossvcserver("experimental_service","experiments/example",@serviceCallback, "DataFormat","struct");
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
    % Camera instrinsic parameters
    K = [531.16719459, 0,686.90394518; 0, 532.5711697, 364.00099154; 0, 0, 1];
    % Radial distortion coefficients
    RadialDist = [-0.31429497,  0.09157624, -0.01083083];
    % Tangential distortion coefficients
    TangentialDist = [-0.00064995,  0.00094649];
    % Camera parameters
    cameraParams = cameraParameters('K',K, ...
    'TangentialDistortion',TangentialDist, ...
    'RadialDistortion',RadialDist);
    % class(defaultRespMsg)
    % properties(defaultRespMsg)
    % properties(reqMsg)
    x_dist = reqMsg.XDist;
    y_dist = reqMsg.YDist;
    dist_points = [x_dist, y_dist];
    udis_points = undistortPoints(dist_points,cameraParams);
    response = defaultRespMsg;
    class(response)
    % response = ros.msggen.experiments.exampleResponse;
    % class(defaultRespMsg)
    response.XUndis = udis_points(1);
    response.YUndis = udis_points(2);
end

end