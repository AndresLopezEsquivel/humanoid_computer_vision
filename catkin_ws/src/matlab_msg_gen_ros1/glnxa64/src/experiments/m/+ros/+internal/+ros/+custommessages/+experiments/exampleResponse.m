function [data, info] = exampleResponse
%example gives an empty data for experiments/exampleResponse
% Copyright 2019-2020 The MathWorks, Inc.
%#codegen
data = struct();
data.MessageType = 'experiments/exampleResponse';
[data.XUndis, info.XUndis] = ros.internal.ros.messages.ros.default_type('double',1);
[data.YUndis, info.YUndis] = ros.internal.ros.messages.ros.default_type('double',1);
info.MessageType = 'experiments/exampleResponse';
info.constant = 0;
info.default = 0;
info.maxstrlen = NaN;
info.MaxLen = 1;
info.MinLen = 1;
info.MatPath = cell(1,2);
info.MatPath{1} = 'x_undis';
info.MatPath{2} = 'y_undis';
