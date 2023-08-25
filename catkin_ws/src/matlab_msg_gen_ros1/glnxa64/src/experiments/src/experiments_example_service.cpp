// Copyright 2019-2021 The MathWorks, Inc.
// Common copy functions for experiments/exampleRequest
#include "boost/date_time.hpp"
#include "boost/shared_array.hpp"
#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4244)
#pragma warning(disable : 4265)
#pragma warning(disable : 4458)
#pragma warning(disable : 4100)
#pragma warning(disable : 4127)
#pragma warning(disable : 4267)
#pragma warning(disable : 4068)
#pragma warning(disable : 4245)
#else
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wpedantic"
#pragma GCC diagnostic ignored "-Wunused-local-typedefs"
#pragma GCC diagnostic ignored "-Wredundant-decls"
#pragma GCC diagnostic ignored "-Wnon-virtual-dtor"
#pragma GCC diagnostic ignored "-Wdelete-non-virtual-dtor"
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wshadow"
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif //_MSC_VER
#include "ros/ros.h"
#include "experiments/example.h"
#include "visibility_control.h"
#include "ROSPubSubTemplates.hpp"
#include "ROSServiceTemplates.hpp"
class EXPERIMENTS_EXPORT experiments_msg_exampleRequest_common : public MATLABROSMsgInterface<experiments::example::Request> {
  public:
    virtual ~experiments_msg_exampleRequest_common(){}
    virtual void copy_from_struct(experiments::example::Request* msg, const matlab::data::Struct& arr, MultiLibLoader loader); 
    //----------------------------------------------------------------------------
    virtual MDArray_T get_arr(MDFactory_T& factory, const experiments::example::Request* msg, MultiLibLoader loader, size_t size = 1);
};
  void experiments_msg_exampleRequest_common::copy_from_struct(experiments::example::Request* msg, const matlab::data::Struct& arr,
               MultiLibLoader loader) {
    try {
        //x_dist
        const matlab::data::TypedArray<double> x_dist_arr = arr["XDist"];
        msg->x_dist = x_dist_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'XDist' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'XDist' is wrong type; expected a double.");
    }
    try {
        //y_dist
        const matlab::data::TypedArray<double> y_dist_arr = arr["YDist"];
        msg->y_dist = y_dist_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'YDist' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'YDist' is wrong type; expected a double.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T experiments_msg_exampleRequest_common::get_arr(MDFactory_T& factory, const experiments::example::Request* msg,
       MultiLibLoader loader, size_t size) {
    auto outArray = factory.createStructArray({size,1},{"MessageType","XDist","YDist"});
    for(size_t ctr = 0; ctr < size; ctr++){
    outArray[ctr]["MessageType"] = factory.createCharArray("experiments/exampleRequest");
    // x_dist
    auto currentElement_x_dist = (msg + ctr)->x_dist;
    outArray[ctr]["XDist"] = factory.createScalar(currentElement_x_dist);
    // y_dist
    auto currentElement_y_dist = (msg + ctr)->y_dist;
    outArray[ctr]["YDist"] = factory.createScalar(currentElement_y_dist);
    }
    return std::move(outArray);
  }
class EXPERIMENTS_EXPORT experiments_msg_exampleResponse_common : public MATLABROSMsgInterface<experiments::example::Response> {
  public:
    virtual ~experiments_msg_exampleResponse_common(){}
    virtual void copy_from_struct(experiments::example::Response* msg, const matlab::data::Struct& arr, MultiLibLoader loader); 
    //----------------------------------------------------------------------------
    virtual MDArray_T get_arr(MDFactory_T& factory, const experiments::example::Response* msg, MultiLibLoader loader, size_t size = 1);
};
  void experiments_msg_exampleResponse_common::copy_from_struct(experiments::example::Response* msg, const matlab::data::Struct& arr,
               MultiLibLoader loader) {
    try {
        //x_undis
        const matlab::data::TypedArray<double> x_undis_arr = arr["XUndis"];
        msg->x_undis = x_undis_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'XUndis' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'XUndis' is wrong type; expected a double.");
    }
    try {
        //y_undis
        const matlab::data::TypedArray<double> y_undis_arr = arr["YUndis"];
        msg->y_undis = y_undis_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'YUndis' is missing.");
    } catch (matlab::Exception&) {
        throw std::invalid_argument("Field 'YUndis' is wrong type; expected a double.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T experiments_msg_exampleResponse_common::get_arr(MDFactory_T& factory, const experiments::example::Response* msg,
       MultiLibLoader loader, size_t size) {
    auto outArray = factory.createStructArray({size,1},{"MessageType","XUndis","YUndis"});
    for(size_t ctr = 0; ctr < size; ctr++){
    outArray[ctr]["MessageType"] = factory.createCharArray("experiments/exampleResponse");
    // x_undis
    auto currentElement_x_undis = (msg + ctr)->x_undis;
    outArray[ctr]["XUndis"] = factory.createScalar(currentElement_x_undis);
    // y_undis
    auto currentElement_y_undis = (msg + ctr)->y_undis;
    outArray[ctr]["YUndis"] = factory.createScalar(currentElement_y_undis);
    }
    return std::move(outArray);
  } 
class EXPERIMENTS_EXPORT experiments_example_service : public ROSMsgElementInterfaceFactory {
  public:
    virtual ~experiments_example_service(){}
    virtual std::shared_ptr<MATLABPublisherInterface> generatePublisherInterface(ElementType type);
    virtual std::shared_ptr<MATLABSubscriberInterface> generateSubscriberInterface(ElementType type);
    virtual std::shared_ptr<MATLABRosbagWriterInterface> generateRosbagWriterInterface(ElementType type);
    virtual std::shared_ptr<MATLABSvcServerInterface> generateSvcServerInterface();
    virtual std::shared_ptr<MATLABSvcClientInterface> generateSvcClientInterface();
};  
  std::shared_ptr<MATLABPublisherInterface> 
          experiments_example_service::generatePublisherInterface(ElementType type){
    std::shared_ptr<MATLABPublisherInterface> ptr;
    if(type == eRequest){
        ptr = std::make_shared<ROSPublisherImpl<experiments::example::Request,experiments_msg_exampleRequest_common>>();
    }else if(type == eResponse){
        ptr = std::make_shared<ROSPublisherImpl<experiments::example::Response,experiments_msg_exampleResponse_common>>();
    }else{
        throw std::invalid_argument("Wrong input, Expected 'Request' or 'Response'");
    }
    return ptr;
  }
  std::shared_ptr<MATLABSubscriberInterface> 
          experiments_example_service::generateSubscriberInterface(ElementType type){
    std::shared_ptr<MATLABSubscriberInterface> ptr;
    if(type == eRequest){
        ptr = std::make_shared<ROSSubscriberImpl<experiments::example::Request,experiments::example::Request::ConstPtr,experiments_msg_exampleRequest_common>>();
    }else if(type == eResponse){
        ptr = std::make_shared<ROSSubscriberImpl<experiments::example::Response,experiments::example::Response::ConstPtr,experiments_msg_exampleResponse_common>>();
    }else{
        throw std::invalid_argument("Wrong input, Expected 'Request' or 'Response'");
    }
    return ptr;
  }
  std::shared_ptr<MATLABSvcServerInterface> 
          experiments_example_service::generateSvcServerInterface(){
    return std::make_shared<ROSSvcServerImpl<experiments::example::Request,experiments::example::Response,experiments_msg_exampleRequest_common,experiments_msg_exampleResponse_common>>();
  }
  std::shared_ptr<MATLABSvcClientInterface> 
          experiments_example_service::generateSvcClientInterface(){
    return std::make_shared<ROSSvcClientImpl<experiments::example,experiments::example::Request,experiments::example::Response,experiments_msg_exampleRequest_common,experiments_msg_exampleResponse_common>>();
  }
#include "ROSbagTemplates.hpp" 
  std::shared_ptr<MATLABRosbagWriterInterface> 
          experiments_example_service::generateRosbagWriterInterface(ElementType type){
    std::shared_ptr<MATLABRosbagWriterInterface> ptr;
    if(type == eRequest){
        ptr = std::make_shared<ROSBagWriterImpl<experiments::exampleRequest,experiments_msg_exampleRequest_common>>();
    }else if(type == eResponse){
        ptr = std::make_shared<ROSBagWriterImpl<experiments::exampleResponse,experiments_msg_exampleResponse_common>>();
    }else{
        throw std::invalid_argument("Wrong input, Expected 'Request' or 'Response'");
    }
    return ptr;
  }
#include "register_macro.hpp"
// Register the component with class_loader.
// This acts as a sort of entry point, allowing the component to be discoverable when its library
// is being loaded into a running process.
CLASS_LOADER_REGISTER_CLASS(experiments_msg_exampleRequest_common, MATLABROSMsgInterface<experiments::exampleRequest>)
CLASS_LOADER_REGISTER_CLASS(experiments_msg_exampleResponse_common, MATLABROSMsgInterface<experiments::exampleResponse>)
CLASS_LOADER_REGISTER_CLASS(experiments_example_service, ROSMsgElementInterfaceFactory)
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif //_MSC_VER
//gen-1
