// Auto-generated. Do not edit!

// (in-package n3ctrl.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ControllerDebug {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.des_p = null;
      this.u_p_p = null;
      this.u_p_i = null;
      this.u_p = null;
      this.des_v = null;
      this.u_v_p = null;
      this.u_v_i = null;
      this.u_v = null;
      this.k_p_p = null;
      this.k_p_i = null;
      this.k_v_p = null;
      this.k_v_i = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('des_p')) {
        this.des_p = initObj.des_p
      }
      else {
        this.des_p = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('u_p_p')) {
        this.u_p_p = initObj.u_p_p
      }
      else {
        this.u_p_p = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('u_p_i')) {
        this.u_p_i = initObj.u_p_i
      }
      else {
        this.u_p_i = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('u_p')) {
        this.u_p = initObj.u_p
      }
      else {
        this.u_p = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('des_v')) {
        this.des_v = initObj.des_v
      }
      else {
        this.des_v = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('u_v_p')) {
        this.u_v_p = initObj.u_v_p
      }
      else {
        this.u_v_p = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('u_v_i')) {
        this.u_v_i = initObj.u_v_i
      }
      else {
        this.u_v_i = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('u_v')) {
        this.u_v = initObj.u_v
      }
      else {
        this.u_v = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('k_p_p')) {
        this.k_p_p = initObj.k_p_p
      }
      else {
        this.k_p_p = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('k_p_i')) {
        this.k_p_i = initObj.k_p_i
      }
      else {
        this.k_p_i = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('k_v_p')) {
        this.k_v_p = initObj.k_v_p
      }
      else {
        this.k_v_p = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('k_v_i')) {
        this.k_v_i = initObj.k_v_i
      }
      else {
        this.k_v_i = new geometry_msgs.msg.Vector3();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ControllerDebug
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [des_p]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.des_p, buffer, bufferOffset);
    // Serialize message field [u_p_p]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.u_p_p, buffer, bufferOffset);
    // Serialize message field [u_p_i]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.u_p_i, buffer, bufferOffset);
    // Serialize message field [u_p]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.u_p, buffer, bufferOffset);
    // Serialize message field [des_v]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.des_v, buffer, bufferOffset);
    // Serialize message field [u_v_p]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.u_v_p, buffer, bufferOffset);
    // Serialize message field [u_v_i]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.u_v_i, buffer, bufferOffset);
    // Serialize message field [u_v]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.u_v, buffer, bufferOffset);
    // Serialize message field [k_p_p]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.k_p_p, buffer, bufferOffset);
    // Serialize message field [k_p_i]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.k_p_i, buffer, bufferOffset);
    // Serialize message field [k_v_p]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.k_v_p, buffer, bufferOffset);
    // Serialize message field [k_v_i]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.k_v_i, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ControllerDebug
    let len;
    let data = new ControllerDebug(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [des_p]
    data.des_p = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [u_p_p]
    data.u_p_p = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [u_p_i]
    data.u_p_i = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [u_p]
    data.u_p = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [des_v]
    data.des_v = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [u_v_p]
    data.u_v_p = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [u_v_i]
    data.u_v_i = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [u_v]
    data.u_v = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [k_p_p]
    data.k_p_p = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [k_p_i]
    data.k_p_i = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [k_v_p]
    data.k_v_p = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [k_v_i]
    data.k_v_i = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 288;
  }

  static datatype() {
    // Returns string type for a message object
    return 'n3ctrl/ControllerDebug';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2879e490b09bd2d41232bc7fbaf6a3c1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ControllerDebug(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.des_p !== undefined) {
      resolved.des_p = geometry_msgs.msg.Vector3.Resolve(msg.des_p)
    }
    else {
      resolved.des_p = new geometry_msgs.msg.Vector3()
    }

    if (msg.u_p_p !== undefined) {
      resolved.u_p_p = geometry_msgs.msg.Vector3.Resolve(msg.u_p_p)
    }
    else {
      resolved.u_p_p = new geometry_msgs.msg.Vector3()
    }

    if (msg.u_p_i !== undefined) {
      resolved.u_p_i = geometry_msgs.msg.Vector3.Resolve(msg.u_p_i)
    }
    else {
      resolved.u_p_i = new geometry_msgs.msg.Vector3()
    }

    if (msg.u_p !== undefined) {
      resolved.u_p = geometry_msgs.msg.Vector3.Resolve(msg.u_p)
    }
    else {
      resolved.u_p = new geometry_msgs.msg.Vector3()
    }

    if (msg.des_v !== undefined) {
      resolved.des_v = geometry_msgs.msg.Vector3.Resolve(msg.des_v)
    }
    else {
      resolved.des_v = new geometry_msgs.msg.Vector3()
    }

    if (msg.u_v_p !== undefined) {
      resolved.u_v_p = geometry_msgs.msg.Vector3.Resolve(msg.u_v_p)
    }
    else {
      resolved.u_v_p = new geometry_msgs.msg.Vector3()
    }

    if (msg.u_v_i !== undefined) {
      resolved.u_v_i = geometry_msgs.msg.Vector3.Resolve(msg.u_v_i)
    }
    else {
      resolved.u_v_i = new geometry_msgs.msg.Vector3()
    }

    if (msg.u_v !== undefined) {
      resolved.u_v = geometry_msgs.msg.Vector3.Resolve(msg.u_v)
    }
    else {
      resolved.u_v = new geometry_msgs.msg.Vector3()
    }

    if (msg.k_p_p !== undefined) {
      resolved.k_p_p = geometry_msgs.msg.Vector3.Resolve(msg.k_p_p)
    }
    else {
      resolved.k_p_p = new geometry_msgs.msg.Vector3()
    }

    if (msg.k_p_i !== undefined) {
      resolved.k_p_i = geometry_msgs.msg.Vector3.Resolve(msg.k_p_i)
    }
    else {
      resolved.k_p_i = new geometry_msgs.msg.Vector3()
    }

    if (msg.k_v_p !== undefined) {
      resolved.k_v_p = geometry_msgs.msg.Vector3.Resolve(msg.k_v_p)
    }
    else {
      resolved.k_v_p = new geometry_msgs.msg.Vector3()
    }

    if (msg.k_v_i !== undefined) {
      resolved.k_v_i = geometry_msgs.msg.Vector3.Resolve(msg.k_v_i)
    }
    else {
      resolved.k_v_i = new geometry_msgs.msg.Vector3()
    }

    return resolved;
    }
};

module.exports = ControllerDebug;
