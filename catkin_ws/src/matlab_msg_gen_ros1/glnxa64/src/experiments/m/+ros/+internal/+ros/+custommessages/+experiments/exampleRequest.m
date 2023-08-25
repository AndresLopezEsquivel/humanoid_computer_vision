function [data, info] = exampleRequest
%example gives an empty data for experiments/exampleRequest
% Copyright 2019-2020 The MathWorks, Inc.
%#codegen
data = struct();
data.MessageType = 'experiments/exampleRequest';
[data.XDist, info.XDist] = ros.internal.ros.messages.ros.default_type('double',1);
[data.YDist, info.YDist] = ros.internal.ros.messages.ros.default_type('double',1);
info.MessageType = 'experiments/exampleRequest';
info.constant = 0;
info.default = 0;
info.maxstrlen = NaN;
info.MaxLen = 1;
info.MinLen = 1;
info.MatPath = cell(1,2);
info.MatPath{1} = 'x_dist';
info.MatPath{2} = 'y_dist';
