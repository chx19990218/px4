;; Auto-generated. Do not edit!


(when (boundp 'n3ctrl::ControllerDebug)
  (if (not (find-package "N3CTRL"))
    (make-package "N3CTRL"))
  (shadow 'ControllerDebug (find-package "N3CTRL")))
(unless (find-package "N3CTRL::CONTROLLERDEBUG")
  (make-package "N3CTRL::CONTROLLERDEBUG"))

(in-package "ROS")
;;//! \htmlinclude ControllerDebug.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass n3ctrl::ControllerDebug
  :super ros::object
  :slots (_header _des_p _u_p_p _u_p_i _u_p _des_v _u_v_p _u_v_i _u_v _k_p_p _k_p_i _k_v_p _k_v_i ))

(defmethod n3ctrl::ControllerDebug
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:des_p __des_p) (instance geometry_msgs::Vector3 :init))
    ((:u_p_p __u_p_p) (instance geometry_msgs::Vector3 :init))
    ((:u_p_i __u_p_i) (instance geometry_msgs::Vector3 :init))
    ((:u_p __u_p) (instance geometry_msgs::Vector3 :init))
    ((:des_v __des_v) (instance geometry_msgs::Vector3 :init))
    ((:u_v_p __u_v_p) (instance geometry_msgs::Vector3 :init))
    ((:u_v_i __u_v_i) (instance geometry_msgs::Vector3 :init))
    ((:u_v __u_v) (instance geometry_msgs::Vector3 :init))
    ((:k_p_p __k_p_p) (instance geometry_msgs::Vector3 :init))
    ((:k_p_i __k_p_i) (instance geometry_msgs::Vector3 :init))
    ((:k_v_p __k_v_p) (instance geometry_msgs::Vector3 :init))
    ((:k_v_i __k_v_i) (instance geometry_msgs::Vector3 :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _des_p __des_p)
   (setq _u_p_p __u_p_p)
   (setq _u_p_i __u_p_i)
   (setq _u_p __u_p)
   (setq _des_v __des_v)
   (setq _u_v_p __u_v_p)
   (setq _u_v_i __u_v_i)
   (setq _u_v __u_v)
   (setq _k_p_p __k_p_p)
   (setq _k_p_i __k_p_i)
   (setq _k_v_p __k_v_p)
   (setq _k_v_i __k_v_i)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:des_p
   (&rest __des_p)
   (if (keywordp (car __des_p))
       (send* _des_p __des_p)
     (progn
       (if __des_p (setq _des_p (car __des_p)))
       _des_p)))
  (:u_p_p
   (&rest __u_p_p)
   (if (keywordp (car __u_p_p))
       (send* _u_p_p __u_p_p)
     (progn
       (if __u_p_p (setq _u_p_p (car __u_p_p)))
       _u_p_p)))
  (:u_p_i
   (&rest __u_p_i)
   (if (keywordp (car __u_p_i))
       (send* _u_p_i __u_p_i)
     (progn
       (if __u_p_i (setq _u_p_i (car __u_p_i)))
       _u_p_i)))
  (:u_p
   (&rest __u_p)
   (if (keywordp (car __u_p))
       (send* _u_p __u_p)
     (progn
       (if __u_p (setq _u_p (car __u_p)))
       _u_p)))
  (:des_v
   (&rest __des_v)
   (if (keywordp (car __des_v))
       (send* _des_v __des_v)
     (progn
       (if __des_v (setq _des_v (car __des_v)))
       _des_v)))
  (:u_v_p
   (&rest __u_v_p)
   (if (keywordp (car __u_v_p))
       (send* _u_v_p __u_v_p)
     (progn
       (if __u_v_p (setq _u_v_p (car __u_v_p)))
       _u_v_p)))
  (:u_v_i
   (&rest __u_v_i)
   (if (keywordp (car __u_v_i))
       (send* _u_v_i __u_v_i)
     (progn
       (if __u_v_i (setq _u_v_i (car __u_v_i)))
       _u_v_i)))
  (:u_v
   (&rest __u_v)
   (if (keywordp (car __u_v))
       (send* _u_v __u_v)
     (progn
       (if __u_v (setq _u_v (car __u_v)))
       _u_v)))
  (:k_p_p
   (&rest __k_p_p)
   (if (keywordp (car __k_p_p))
       (send* _k_p_p __k_p_p)
     (progn
       (if __k_p_p (setq _k_p_p (car __k_p_p)))
       _k_p_p)))
  (:k_p_i
   (&rest __k_p_i)
   (if (keywordp (car __k_p_i))
       (send* _k_p_i __k_p_i)
     (progn
       (if __k_p_i (setq _k_p_i (car __k_p_i)))
       _k_p_i)))
  (:k_v_p
   (&rest __k_v_p)
   (if (keywordp (car __k_v_p))
       (send* _k_v_p __k_v_p)
     (progn
       (if __k_v_p (setq _k_v_p (car __k_v_p)))
       _k_v_p)))
  (:k_v_i
   (&rest __k_v_i)
   (if (keywordp (car __k_v_i))
       (send* _k_v_i __k_v_i)
     (progn
       (if __k_v_i (setq _k_v_i (car __k_v_i)))
       _k_v_i)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Vector3 _des_p
    (send _des_p :serialization-length)
    ;; geometry_msgs/Vector3 _u_p_p
    (send _u_p_p :serialization-length)
    ;; geometry_msgs/Vector3 _u_p_i
    (send _u_p_i :serialization-length)
    ;; geometry_msgs/Vector3 _u_p
    (send _u_p :serialization-length)
    ;; geometry_msgs/Vector3 _des_v
    (send _des_v :serialization-length)
    ;; geometry_msgs/Vector3 _u_v_p
    (send _u_v_p :serialization-length)
    ;; geometry_msgs/Vector3 _u_v_i
    (send _u_v_i :serialization-length)
    ;; geometry_msgs/Vector3 _u_v
    (send _u_v :serialization-length)
    ;; geometry_msgs/Vector3 _k_p_p
    (send _k_p_p :serialization-length)
    ;; geometry_msgs/Vector3 _k_p_i
    (send _k_p_i :serialization-length)
    ;; geometry_msgs/Vector3 _k_v_p
    (send _k_v_p :serialization-length)
    ;; geometry_msgs/Vector3 _k_v_i
    (send _k_v_i :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Vector3 _des_p
       (send _des_p :serialize s)
     ;; geometry_msgs/Vector3 _u_p_p
       (send _u_p_p :serialize s)
     ;; geometry_msgs/Vector3 _u_p_i
       (send _u_p_i :serialize s)
     ;; geometry_msgs/Vector3 _u_p
       (send _u_p :serialize s)
     ;; geometry_msgs/Vector3 _des_v
       (send _des_v :serialize s)
     ;; geometry_msgs/Vector3 _u_v_p
       (send _u_v_p :serialize s)
     ;; geometry_msgs/Vector3 _u_v_i
       (send _u_v_i :serialize s)
     ;; geometry_msgs/Vector3 _u_v
       (send _u_v :serialize s)
     ;; geometry_msgs/Vector3 _k_p_p
       (send _k_p_p :serialize s)
     ;; geometry_msgs/Vector3 _k_p_i
       (send _k_p_i :serialize s)
     ;; geometry_msgs/Vector3 _k_v_p
       (send _k_v_p :serialize s)
     ;; geometry_msgs/Vector3 _k_v_i
       (send _k_v_i :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Vector3 _des_p
     (send _des_p :deserialize buf ptr-) (incf ptr- (send _des_p :serialization-length))
   ;; geometry_msgs/Vector3 _u_p_p
     (send _u_p_p :deserialize buf ptr-) (incf ptr- (send _u_p_p :serialization-length))
   ;; geometry_msgs/Vector3 _u_p_i
     (send _u_p_i :deserialize buf ptr-) (incf ptr- (send _u_p_i :serialization-length))
   ;; geometry_msgs/Vector3 _u_p
     (send _u_p :deserialize buf ptr-) (incf ptr- (send _u_p :serialization-length))
   ;; geometry_msgs/Vector3 _des_v
     (send _des_v :deserialize buf ptr-) (incf ptr- (send _des_v :serialization-length))
   ;; geometry_msgs/Vector3 _u_v_p
     (send _u_v_p :deserialize buf ptr-) (incf ptr- (send _u_v_p :serialization-length))
   ;; geometry_msgs/Vector3 _u_v_i
     (send _u_v_i :deserialize buf ptr-) (incf ptr- (send _u_v_i :serialization-length))
   ;; geometry_msgs/Vector3 _u_v
     (send _u_v :deserialize buf ptr-) (incf ptr- (send _u_v :serialization-length))
   ;; geometry_msgs/Vector3 _k_p_p
     (send _k_p_p :deserialize buf ptr-) (incf ptr- (send _k_p_p :serialization-length))
   ;; geometry_msgs/Vector3 _k_p_i
     (send _k_p_i :deserialize buf ptr-) (incf ptr- (send _k_p_i :serialization-length))
   ;; geometry_msgs/Vector3 _k_v_p
     (send _k_v_p :deserialize buf ptr-) (incf ptr- (send _k_v_p :serialization-length))
   ;; geometry_msgs/Vector3 _k_v_i
     (send _k_v_i :deserialize buf ptr-) (incf ptr- (send _k_v_i :serialization-length))
   ;;
   self)
  )

(setf (get n3ctrl::ControllerDebug :md5sum-) "2879e490b09bd2d41232bc7fbaf6a3c1")
(setf (get n3ctrl::ControllerDebug :datatype-) "n3ctrl/ControllerDebug")
(setf (get n3ctrl::ControllerDebug :definition-)
      "Header header
geometry_msgs/Vector3 des_p
geometry_msgs/Vector3 u_p_p
geometry_msgs/Vector3 u_p_i
geometry_msgs/Vector3 u_p
geometry_msgs/Vector3 des_v
geometry_msgs/Vector3 u_v_p
geometry_msgs/Vector3 u_v_i
geometry_msgs/Vector3 u_v
geometry_msgs/Vector3 k_p_p
geometry_msgs/Vector3 k_p_i
geometry_msgs/Vector3 k_v_p
geometry_msgs/Vector3 k_v_i

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :n3ctrl/ControllerDebug "2879e490b09bd2d41232bc7fbaf6a3c1")


