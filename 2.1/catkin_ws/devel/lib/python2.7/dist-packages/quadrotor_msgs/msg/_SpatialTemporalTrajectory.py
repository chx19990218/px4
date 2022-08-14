# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from quadrotor_msgs/SpatialTemporalTrajectory.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import std_msgs.msg

class SpatialTemporalTrajectory(genpy.Message):
  _md5sum = "83bb3014c3955b8c85e7aaebbe585ea5"
  _type = "quadrotor_msgs/SpatialTemporalTrajectory"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

time start_time
time final_time

# the trajectory id, starts from "1".
uint32 trajectory_id

# the action command for trajectory server.
uint32 ACTION_ADD                  =   1
uint32 ACTION_ABORT                =   2
uint32 ACTION_WARN_START           =   3
uint32 ACTION_WARN_FINAL           =   4
uint32 ACTION_WARN_IMPOSSIBLE      =   5
uint32 action

# the vector of all 'K' number of each piece of the time profile.
int32[] K
int32   K_max

# the a, b, c, d parameters of the TOPP time profile.
float64[] a
float64[] b

# useful variables for evaluating time
float64[] s
float64[] time
float64[] time_acc

# delta_s in s domain
float64   s_step

# the order of trajectory.
uint32 num_order
uint32 num_segment

# the polynomial coecfficients of the trajectory.
float64 start_yaw
float64 final_yaw
float64[] coef_x
float64[] coef_y
float64[] coef_z
float64[] range
float64   mag_coeff
uint32[]  order

string debug_info
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
"""
  # Pseudo-constants
  ACTION_ADD = 1
  ACTION_ABORT = 2
  ACTION_WARN_START = 3
  ACTION_WARN_FINAL = 4
  ACTION_WARN_IMPOSSIBLE = 5

  __slots__ = ['header','start_time','final_time','trajectory_id','action','K','K_max','a','b','s','time','time_acc','s_step','num_order','num_segment','start_yaw','final_yaw','coef_x','coef_y','coef_z','range','mag_coeff','order','debug_info']
  _slot_types = ['std_msgs/Header','time','time','uint32','uint32','int32[]','int32','float64[]','float64[]','float64[]','float64[]','float64[]','float64','uint32','uint32','float64','float64','float64[]','float64[]','float64[]','float64[]','float64','uint32[]','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,start_time,final_time,trajectory_id,action,K,K_max,a,b,s,time,time_acc,s_step,num_order,num_segment,start_yaw,final_yaw,coef_x,coef_y,coef_z,range,mag_coeff,order,debug_info

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SpatialTemporalTrajectory, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.final_time is None:
        self.final_time = genpy.Time()
      if self.trajectory_id is None:
        self.trajectory_id = 0
      if self.action is None:
        self.action = 0
      if self.K is None:
        self.K = []
      if self.K_max is None:
        self.K_max = 0
      if self.a is None:
        self.a = []
      if self.b is None:
        self.b = []
      if self.s is None:
        self.s = []
      if self.time is None:
        self.time = []
      if self.time_acc is None:
        self.time_acc = []
      if self.s_step is None:
        self.s_step = 0.
      if self.num_order is None:
        self.num_order = 0
      if self.num_segment is None:
        self.num_segment = 0
      if self.start_yaw is None:
        self.start_yaw = 0.
      if self.final_yaw is None:
        self.final_yaw = 0.
      if self.coef_x is None:
        self.coef_x = []
      if self.coef_y is None:
        self.coef_y = []
      if self.coef_z is None:
        self.coef_z = []
      if self.range is None:
        self.range = []
      if self.mag_coeff is None:
        self.mag_coeff = 0.
      if self.order is None:
        self.order = []
      if self.debug_info is None:
        self.debug_info = ''
    else:
      self.header = std_msgs.msg.Header()
      self.start_time = genpy.Time()
      self.final_time = genpy.Time()
      self.trajectory_id = 0
      self.action = 0
      self.K = []
      self.K_max = 0
      self.a = []
      self.b = []
      self.s = []
      self.time = []
      self.time_acc = []
      self.s_step = 0.
      self.num_order = 0
      self.num_segment = 0
      self.start_yaw = 0.
      self.final_yaw = 0.
      self.coef_x = []
      self.coef_y = []
      self.coef_z = []
      self.range = []
      self.mag_coeff = 0.
      self.order = []
      self.debug_info = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6I().pack(_x.start_time.secs, _x.start_time.nsecs, _x.final_time.secs, _x.final_time.nsecs, _x.trajectory_id, _x.action))
      length = len(self.K)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.K))
      _x = self.K_max
      buff.write(_get_struct_i().pack(_x))
      length = len(self.a)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.a))
      length = len(self.b)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.b))
      length = len(self.s)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.s))
      length = len(self.time)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.time))
      length = len(self.time_acc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.time_acc))
      _x = self
      buff.write(_get_struct_d2I2d().pack(_x.s_step, _x.num_order, _x.num_segment, _x.start_yaw, _x.final_yaw))
      length = len(self.coef_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.coef_x))
      length = len(self.coef_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.coef_y))
      length = len(self.coef_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.coef_z))
      length = len(self.range)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.range))
      _x = self.mag_coeff
      buff.write(_get_struct_d().pack(_x))
      length = len(self.order)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.order))
      _x = self.debug_info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.final_time is None:
        self.final_time = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.start_time.secs, _x.start_time.nsecs, _x.final_time.secs, _x.final_time.nsecs, _x.trajectory_id, _x.action,) = _get_struct_6I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.K = s.unpack(str[start:end])
      start = end
      end += 4
      (self.K_max,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.a = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.b = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.s = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.time = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.time_acc = s.unpack(str[start:end])
      _x = self
      start = end
      end += 32
      (_x.s_step, _x.num_order, _x.num_segment, _x.start_yaw, _x.final_yaw,) = _get_struct_d2I2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coef_x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coef_y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coef_z = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.range = s.unpack(str[start:end])
      start = end
      end += 8
      (self.mag_coeff,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.order = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.debug_info = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.debug_info = str[start:end]
      self.start_time.canon()
      self.final_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6I().pack(_x.start_time.secs, _x.start_time.nsecs, _x.final_time.secs, _x.final_time.nsecs, _x.trajectory_id, _x.action))
      length = len(self.K)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.K.tostring())
      _x = self.K_max
      buff.write(_get_struct_i().pack(_x))
      length = len(self.a)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.a.tostring())
      length = len(self.b)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.b.tostring())
      length = len(self.s)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.s.tostring())
      length = len(self.time)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.time.tostring())
      length = len(self.time_acc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.time_acc.tostring())
      _x = self
      buff.write(_get_struct_d2I2d().pack(_x.s_step, _x.num_order, _x.num_segment, _x.start_yaw, _x.final_yaw))
      length = len(self.coef_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.coef_x.tostring())
      length = len(self.coef_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.coef_y.tostring())
      length = len(self.coef_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.coef_z.tostring())
      length = len(self.range)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.range.tostring())
      _x = self.mag_coeff
      buff.write(_get_struct_d().pack(_x))
      length = len(self.order)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.order.tostring())
      _x = self.debug_info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.final_time is None:
        self.final_time = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.start_time.secs, _x.start_time.nsecs, _x.final_time.secs, _x.final_time.nsecs, _x.trajectory_id, _x.action,) = _get_struct_6I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.K = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (self.K_max,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.a = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.b = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.s = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.time = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.time_acc = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 32
      (_x.s_step, _x.num_order, _x.num_segment, _x.start_yaw, _x.final_yaw,) = _get_struct_d2I2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coef_x = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coef_y = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.coef_z = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.range = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 8
      (self.mag_coeff,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.order = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.debug_info = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.debug_info = str[start:end]
      self.start_time.canon()
      self.final_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_6I = None
def _get_struct_6I():
    global _struct_6I
    if _struct_6I is None:
        _struct_6I = struct.Struct("<6I")
    return _struct_6I
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_d2I2d = None
def _get_struct_d2I2d():
    global _struct_d2I2d
    if _struct_d2I2d is None:
        _struct_d2I2d = struct.Struct("<d2I2d")
    return _struct_d2I2d
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
