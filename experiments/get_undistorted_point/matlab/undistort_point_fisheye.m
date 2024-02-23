% clc; clear;
format long
% % Camera instrinsic parameters
% K = [531.16719459, 0,686.90394518; 0, 532.5711697, 364.00099154; 0, 0, 1];
% % Radial distortion coefficients
% RadialDist = [-0.31429497,  0.09157624, -0.01083083];
% % Tangential distortion coefficients
% TangentialDist = [-0.00064995,  0.00094649];
% % Camera parameters
% cameraParams = cameraParameters('K',K, ...
%     'TangentialDistortion',TangentialDist, ...
%     'RadialDistortion',RadialDist);

mappingCoefficients = [5.420700282657709e+02 -6.365578727668607e-04 -1.845143184037665e-07 -1.434269892513010e-10];
distortionCenter = [6.968767830094720e+02 3.466703380573117e+02];
imageSize = [720 1280];
intrinsics = fisheyeIntrinsics(mappingCoefficients,imageSize,distortionCenter);

y = 0 : 10 : 720;
s = size(y);
x = 0 * ones(1,s(2));
pointsA = horzcat(x',y');

x = 0 : 10 : 1280;
s = size(x);
y = 720 * ones(1,s(2));
pointsB = horzcat(x',y');

y = 720 : -10 : 0;
s = size(y);
x = 1280 * ones(1,s(2));
pointsC = horzcat(x',y');

x = 1280 : -10: 0;
s = size(x);
y = 0 * ones(1,s(2));
pointsD = horzcat(x',y');

points = vertcat(pointsA, pointsB, pointsC, pointsD);

undistortedPoints = undistortFisheyePoints(points,intrinsics);
% undistortedPoints = undistortFisheyePoints(points, cameraParams.Intrinsics);

plot(undistortedPoints(:,1), ...
    undistortedPoints(:,2), ...
     'LineWidth',2);

hold on;

plot(points(:,1), points(:,2), 'LineWidth', 2);

legend('Sin distorsion', 'Con distorsion');
title('Imagenes con y sin distorsion')
xlabel('x [px]')
ylabel('y [px]')

ax = gca;
ax.YDir = 'reverse';

grid;

% saveas(gcf,'points.png')
% hold on;
% plot(x',y','LineWidth',5)
% imds = imageDatastore({'2023-02-12-192429.jpg'});
% img = readimage(imds,1);
% J1 = undistortImage(img,cameraParams);
% imshow(img); figure; imshow(J1)