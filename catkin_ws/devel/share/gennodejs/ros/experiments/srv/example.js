// Auto-generated. Do not edit!

// (in-package experiments.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class exampleRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_dist = null;
      this.y_dist = null;
    }
    else {
      if (initObj.hasOwnProperty('x_dist')) {
        this.x_dist = initObj.x_dist
      }
      else {
        this.x_dist = 0.0;
      }
      if (initObj.hasOwnProperty('y_dist')) {
        this.y_dist = initObj.y_dist
      }
      else {
        this.y_dist = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type exampleRequest
    // Serialize message field [x_dist]
    bufferOffset = _serializer.float64(obj.x_dist, buffer, bufferOffset);
    // Serialize message field [y_dist]
    bufferOffset = _serializer.float64(obj.y_dist, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type exampleRequest
    let len;
    let data = new exampleRequest(null);
    // Deserialize message field [x_dist]
    data.x_dist = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_dist]
    data.y_dist = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'experiments/exampleRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9e9fe6ad89b5212aaaa506f6cbd26357';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # request
    float64 x_dist
    float64 y_dist
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new exampleRequest(null);
    if (msg.x_dist !== undefined) {
      resolved.x_dist = msg.x_dist;
    }
    else {
      resolved.x_dist = 0.0
    }

    if (msg.y_dist !== undefined) {
      resolved.y_dist = msg.y_dist;
    }
    else {
      resolved.y_dist = 0.0
    }

    return resolved;
    }
};

class exampleResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_undis = null;
      this.y_undis = null;
    }
    else {
      if (initObj.hasOwnProperty('x_undis')) {
        this.x_undis = initObj.x_undis
      }
      else {
        this.x_undis = 0.0;
      }
      if (initObj.hasOwnProperty('y_undis')) {
        this.y_undis = initObj.y_undis
      }
      else {
        this.y_undis = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type exampleResponse
    // Serialize message field [x_undis]
    bufferOffset = _serializer.float64(obj.x_undis, buffer, bufferOffset);
    // Serialize message field [y_undis]
    bufferOffset = _serializer.float64(obj.y_undis, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type exampleResponse
    let len;
    let data = new exampleResponse(null);
    // Deserialize message field [x_undis]
    data.x_undis = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_undis]
    data.y_undis = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'experiments/exampleResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0f77863efde0c711a2ca857d4054f51d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # result
    float64 x_undis
    float64 y_undis
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new exampleResponse(null);
    if (msg.x_undis !== undefined) {
      resolved.x_undis = msg.x_undis;
    }
    else {
      resolved.x_undis = 0.0
    }

    if (msg.y_undis !== undefined) {
      resolved.y_undis = msg.y_undis;
    }
    else {
      resolved.y_undis = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: exampleRequest,
  Response: exampleResponse,
  md5sum() { return '76b5930aa6e27a49039927b2ca52db98'; },
  datatype() { return 'experiments/example'; }
};
