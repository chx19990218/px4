# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from quadrotor_msgs/SwarmInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import quadrotor_msgs.msg
import std_msgs.msg

class SwarmInfo(genpy.Message):
  _md5sum = "908ae631e70132160c2527a9926df867"
  _type = "quadrotor_msgs/SwarmInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """quadrotor_msgs/TrajectoryMatrix path
time start

================================================================================
MSG: quadrotor_msgs/TrajectoryMatrix
#type
uint8 TYPE_UNKNOWN = 0
uint8 TYPE_POLY    = 1
uint8 TYPE_TIME    = 2

#data structure
Header    header
uint8     type
uint32    id
string    name
uint32[]  format
float64[] data

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
  __slots__ = ['path','start']
  _slot_types = ['quadrotor_msgs/TrajectoryMatrix','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       path,start

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SwarmInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.path is None:
        self.path = quadrotor_msgs.msg.TrajectoryMatrix()
      if self.start is None:
        self.start = genpy.Time()
    else:
      self.path = quadrotor_msgs.msg.TrajectoryMatrix()
      self.start = genpy.Time()

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
      buff.write(_get_struct_3I().pack(_x.path.header.seq, _x.path.header.stamp.secs, _x.path.header.stamp.nsecs))
      _x = self.path.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.path.type, _x.path.id))
      _x = self.path.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.path.format)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.path.format))
      length = len(self.path.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.path.data))
      _x = self
      buff.write(_get_struct_2I().pack(_x.start.secs, _x.start.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.path is None:
        self.path = quadrotor_msgs.msg.TrajectoryMatrix()
      if self.start is None:
        self.start = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.path.header.seq, _x.path.header.stamp.secs, _x.path.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.path.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.path.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.path.type, _x.path.id,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.path.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.path.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.path.format = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.path.data = s.unpack(str[start:end])
      _x = self
      start = end
      end += 8
      (_x.start.secs, _x.start.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.start.canon()
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
      buff.write(_get_struct_3I().pack(_x.path.header.seq, _x.path.header.stamp.secs, _x.path.header.stamp.nsecs))
      _x = self.path.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.path.type, _x.path.id))
      _x = self.path.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.path.format)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.path.format.tostring())
      length = len(self.path.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.path.data.tostring())
      _x = self
      buff.write(_get_struct_2I().pack(_x.start.secs, _x.start.nsecs))
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
      if self.path is None:
        self.path = quadrotor_msgs.msg.TrajectoryMatrix()
      if self.start is None:
        self.start = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.path.header.seq, _x.path.header.stamp.secs, _x.path.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.path.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.path.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.path.type, _x.path.id,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.path.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.path.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.path.format = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.path.data = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 8
      (_x.start.secs, _x.start.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.start.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
