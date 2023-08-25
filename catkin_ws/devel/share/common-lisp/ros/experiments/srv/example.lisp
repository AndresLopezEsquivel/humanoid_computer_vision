; Auto-generated. Do not edit!


(cl:in-package experiments-srv)


;//! \htmlinclude example-request.msg.html

(cl:defclass <example-request> (roslisp-msg-protocol:ros-message)
  ((x_dist
    :reader x_dist
    :initarg :x_dist
    :type cl:float
    :initform 0.0)
   (y_dist
    :reader y_dist
    :initarg :y_dist
    :type cl:float
    :initform 0.0))
)

(cl:defclass example-request (<example-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <example-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'example-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name experiments-srv:<example-request> is deprecated: use experiments-srv:example-request instead.")))

(cl:ensure-generic-function 'x_dist-val :lambda-list '(m))
(cl:defmethod x_dist-val ((m <example-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader experiments-srv:x_dist-val is deprecated.  Use experiments-srv:x_dist instead.")
  (x_dist m))

(cl:ensure-generic-function 'y_dist-val :lambda-list '(m))
(cl:defmethod y_dist-val ((m <example-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader experiments-srv:y_dist-val is deprecated.  Use experiments-srv:y_dist instead.")
  (y_dist m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <example-request>) ostream)
  "Serializes a message object of type '<example-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x_dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y_dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <example-request>) istream)
  "Deserializes a message object of type '<example-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_dist) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_dist) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<example-request>)))
  "Returns string type for a service object of type '<example-request>"
  "experiments/exampleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'example-request)))
  "Returns string type for a service object of type 'example-request"
  "experiments/exampleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<example-request>)))
  "Returns md5sum for a message object of type '<example-request>"
  "76b5930aa6e27a49039927b2ca52db98")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'example-request)))
  "Returns md5sum for a message object of type 'example-request"
  "76b5930aa6e27a49039927b2ca52db98")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<example-request>)))
  "Returns full string definition for message of type '<example-request>"
  (cl:format cl:nil "# request~%float64 x_dist~%float64 y_dist~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'example-request)))
  "Returns full string definition for message of type 'example-request"
  (cl:format cl:nil "# request~%float64 x_dist~%float64 y_dist~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <example-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <example-request>))
  "Converts a ROS message object to a list"
  (cl:list 'example-request
    (cl:cons ':x_dist (x_dist msg))
    (cl:cons ':y_dist (y_dist msg))
))
;//! \htmlinclude example-response.msg.html

(cl:defclass <example-response> (roslisp-msg-protocol:ros-message)
  ((x_undis
    :reader x_undis
    :initarg :x_undis
    :type cl:float
    :initform 0.0)
   (y_undis
    :reader y_undis
    :initarg :y_undis
    :type cl:float
    :initform 0.0))
)

(cl:defclass example-response (<example-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <example-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'example-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name experiments-srv:<example-response> is deprecated: use experiments-srv:example-response instead.")))

(cl:ensure-generic-function 'x_undis-val :lambda-list '(m))
(cl:defmethod x_undis-val ((m <example-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader experiments-srv:x_undis-val is deprecated.  Use experiments-srv:x_undis instead.")
  (x_undis m))

(cl:ensure-generic-function 'y_undis-val :lambda-list '(m))
(cl:defmethod y_undis-val ((m <example-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader experiments-srv:y_undis-val is deprecated.  Use experiments-srv:y_undis instead.")
  (y_undis m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <example-response>) ostream)
  "Serializes a message object of type '<example-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x_undis))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y_undis))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <example-response>) istream)
  "Deserializes a message object of type '<example-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_undis) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_undis) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<example-response>)))
  "Returns string type for a service object of type '<example-response>"
  "experiments/exampleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'example-response)))
  "Returns string type for a service object of type 'example-response"
  "experiments/exampleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<example-response>)))
  "Returns md5sum for a message object of type '<example-response>"
  "76b5930aa6e27a49039927b2ca52db98")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'example-response)))
  "Returns md5sum for a message object of type 'example-response"
  "76b5930aa6e27a49039927b2ca52db98")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<example-response>)))
  "Returns full string definition for message of type '<example-response>"
  (cl:format cl:nil "# result~%float64 x_undis~%float64 y_undis~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'example-response)))
  "Returns full string definition for message of type 'example-response"
  (cl:format cl:nil "# result~%float64 x_undis~%float64 y_undis~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <example-response>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <example-response>))
  "Converts a ROS message object to a list"
  (cl:list 'example-response
    (cl:cons ':x_undis (x_undis msg))
    (cl:cons ':y_undis (y_undis msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'example)))
  'example-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'example)))
  'example-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'example)))
  "Returns string type for a service object of type '<example>"
  "experiments/example")