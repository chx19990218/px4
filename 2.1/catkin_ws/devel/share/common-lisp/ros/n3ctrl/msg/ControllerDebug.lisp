; Auto-generated. Do not edit!


(cl:in-package n3ctrl-msg)


;//! \htmlinclude ControllerDebug.msg.html

(cl:defclass <ControllerDebug> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (des_p
    :reader des_p
    :initarg :des_p
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u_p_p
    :reader u_p_p
    :initarg :u_p_p
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u_p_i
    :reader u_p_i
    :initarg :u_p_i
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u_p
    :reader u_p
    :initarg :u_p
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (des_v
    :reader des_v
    :initarg :des_v
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u_v_p
    :reader u_v_p
    :initarg :u_v_p
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u_v_i
    :reader u_v_i
    :initarg :u_v_i
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u_v
    :reader u_v
    :initarg :u_v
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (k_p_p
    :reader k_p_p
    :initarg :k_p_p
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (k_p_i
    :reader k_p_i
    :initarg :k_p_i
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (k_v_p
    :reader k_v_p
    :initarg :k_v_p
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (k_v_i
    :reader k_v_i
    :initarg :k_v_i
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass ControllerDebug (<ControllerDebug>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControllerDebug>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControllerDebug)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name n3ctrl-msg:<ControllerDebug> is deprecated: use n3ctrl-msg:ControllerDebug instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:header-val is deprecated.  Use n3ctrl-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'des_p-val :lambda-list '(m))
(cl:defmethod des_p-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:des_p-val is deprecated.  Use n3ctrl-msg:des_p instead.")
  (des_p m))

(cl:ensure-generic-function 'u_p_p-val :lambda-list '(m))
(cl:defmethod u_p_p-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:u_p_p-val is deprecated.  Use n3ctrl-msg:u_p_p instead.")
  (u_p_p m))

(cl:ensure-generic-function 'u_p_i-val :lambda-list '(m))
(cl:defmethod u_p_i-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:u_p_i-val is deprecated.  Use n3ctrl-msg:u_p_i instead.")
  (u_p_i m))

(cl:ensure-generic-function 'u_p-val :lambda-list '(m))
(cl:defmethod u_p-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:u_p-val is deprecated.  Use n3ctrl-msg:u_p instead.")
  (u_p m))

(cl:ensure-generic-function 'des_v-val :lambda-list '(m))
(cl:defmethod des_v-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:des_v-val is deprecated.  Use n3ctrl-msg:des_v instead.")
  (des_v m))

(cl:ensure-generic-function 'u_v_p-val :lambda-list '(m))
(cl:defmethod u_v_p-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:u_v_p-val is deprecated.  Use n3ctrl-msg:u_v_p instead.")
  (u_v_p m))

(cl:ensure-generic-function 'u_v_i-val :lambda-list '(m))
(cl:defmethod u_v_i-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:u_v_i-val is deprecated.  Use n3ctrl-msg:u_v_i instead.")
  (u_v_i m))

(cl:ensure-generic-function 'u_v-val :lambda-list '(m))
(cl:defmethod u_v-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:u_v-val is deprecated.  Use n3ctrl-msg:u_v instead.")
  (u_v m))

(cl:ensure-generic-function 'k_p_p-val :lambda-list '(m))
(cl:defmethod k_p_p-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:k_p_p-val is deprecated.  Use n3ctrl-msg:k_p_p instead.")
  (k_p_p m))

(cl:ensure-generic-function 'k_p_i-val :lambda-list '(m))
(cl:defmethod k_p_i-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:k_p_i-val is deprecated.  Use n3ctrl-msg:k_p_i instead.")
  (k_p_i m))

(cl:ensure-generic-function 'k_v_p-val :lambda-list '(m))
(cl:defmethod k_v_p-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:k_v_p-val is deprecated.  Use n3ctrl-msg:k_v_p instead.")
  (k_v_p m))

(cl:ensure-generic-function 'k_v_i-val :lambda-list '(m))
(cl:defmethod k_v_i-val ((m <ControllerDebug>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader n3ctrl-msg:k_v_i-val is deprecated.  Use n3ctrl-msg:k_v_i instead.")
  (k_v_i m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControllerDebug>) ostream)
  "Serializes a message object of type '<ControllerDebug>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'des_p) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'u_p_p) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'u_p_i) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'u_p) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'des_v) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'u_v_p) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'u_v_i) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'u_v) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'k_p_p) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'k_p_i) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'k_v_p) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'k_v_i) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControllerDebug>) istream)
  "Deserializes a message object of type '<ControllerDebug>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'des_p) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'u_p_p) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'u_p_i) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'u_p) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'des_v) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'u_v_p) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'u_v_i) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'u_v) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'k_p_p) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'k_p_i) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'k_v_p) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'k_v_i) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControllerDebug>)))
  "Returns string type for a message object of type '<ControllerDebug>"
  "n3ctrl/ControllerDebug")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControllerDebug)))
  "Returns string type for a message object of type 'ControllerDebug"
  "n3ctrl/ControllerDebug")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControllerDebug>)))
  "Returns md5sum for a message object of type '<ControllerDebug>"
  "2879e490b09bd2d41232bc7fbaf6a3c1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControllerDebug)))
  "Returns md5sum for a message object of type 'ControllerDebug"
  "2879e490b09bd2d41232bc7fbaf6a3c1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControllerDebug>)))
  "Returns full string definition for message of type '<ControllerDebug>"
  (cl:format cl:nil "Header header~%geometry_msgs/Vector3 des_p~%geometry_msgs/Vector3 u_p_p~%geometry_msgs/Vector3 u_p_i~%geometry_msgs/Vector3 u_p~%geometry_msgs/Vector3 des_v~%geometry_msgs/Vector3 u_v_p~%geometry_msgs/Vector3 u_v_i~%geometry_msgs/Vector3 u_v~%geometry_msgs/Vector3 k_p_p~%geometry_msgs/Vector3 k_p_i~%geometry_msgs/Vector3 k_v_p~%geometry_msgs/Vector3 k_v_i~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControllerDebug)))
  "Returns full string definition for message of type 'ControllerDebug"
  (cl:format cl:nil "Header header~%geometry_msgs/Vector3 des_p~%geometry_msgs/Vector3 u_p_p~%geometry_msgs/Vector3 u_p_i~%geometry_msgs/Vector3 u_p~%geometry_msgs/Vector3 des_v~%geometry_msgs/Vector3 u_v_p~%geometry_msgs/Vector3 u_v_i~%geometry_msgs/Vector3 u_v~%geometry_msgs/Vector3 k_p_p~%geometry_msgs/Vector3 k_p_i~%geometry_msgs/Vector3 k_v_p~%geometry_msgs/Vector3 k_v_i~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControllerDebug>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'des_p))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'u_p_p))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'u_p_i))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'u_p))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'des_v))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'u_v_p))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'u_v_i))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'u_v))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'k_p_p))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'k_p_i))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'k_v_p))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'k_v_i))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControllerDebug>))
  "Converts a ROS message object to a list"
  (cl:list 'ControllerDebug
    (cl:cons ':header (header msg))
    (cl:cons ':des_p (des_p msg))
    (cl:cons ':u_p_p (u_p_p msg))
    (cl:cons ':u_p_i (u_p_i msg))
    (cl:cons ':u_p (u_p msg))
    (cl:cons ':des_v (des_v msg))
    (cl:cons ':u_v_p (u_v_p msg))
    (cl:cons ':u_v_i (u_v_i msg))
    (cl:cons ':u_v (u_v msg))
    (cl:cons ':k_p_p (k_p_p msg))
    (cl:cons ':k_p_i (k_p_i msg))
    (cl:cons ':k_v_p (k_v_p msg))
    (cl:cons ':k_v_i (k_v_i msg))
))
