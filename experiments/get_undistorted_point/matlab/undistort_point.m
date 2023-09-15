% clc; clear;
format long
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
% points = [0,0;
%     640,0;
%     1280,0;
%     1280,360;
%     1280,720;
%     640,720;
%     0,720;
%     0,360;
%     640,360];
% 
% undistortedPoints = undistortPoints(points,cameraParams);

y = 0 : 720;
s = size(y);
x = 0 * ones(1,s(2));
pointsA = horzcat(x',y');

x = 0 : 1280;
s = size(x);
y = 720 * ones(1,s(2));
pointsB = horzcat(x',y');

y = 720 : -1 : 0;
s = size(y);
x = 1280 * ones(1,s(2));
pointsC = horzcat(x',y');

x = 1280 : -1 : 0;
% x = 0 : 1280;
s = size(x);
y = 0 * ones(1,s(2));
pointsD = horzcat(x',y');

points = vertcat(pointsA, pointsB, pointsC, pointsD);
% plot(points(:,1), points(:,2), 'LineWidth', 2);
% hold on;

% points = [0,0;0,1280;1280,360;640,360];

undistortedPoints = undistortPoints(points,cameraParams);

plot(undistortedPoints(:,1), ...
    undistortedPoints(:,2), ...
     'LineWidth',2);

saveas(gcf,'points.png')
% hold on;
% plot(x',y','LineWidth',5)
% imds = imageDatastore({'2023-02-12-192429.jpg'});
% img = readimage(imds,1);
% J1 = undistortImage(img,cameraParams);
% imshow(img); figure; imshow(J1)