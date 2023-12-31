// Generated by gencpp from file experiments/exampleRequest.msg
// DO NOT EDIT!


#ifndef EXPERIMENTS_MESSAGE_EXAMPLEREQUEST_H
#define EXPERIMENTS_MESSAGE_EXAMPLEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace experiments
{
template <class ContainerAllocator>
struct exampleRequest_
{
  typedef exampleRequest_<ContainerAllocator> Type;

  exampleRequest_()
    : x_dist(0.0)
    , y_dist(0.0)  {
    }
  exampleRequest_(const ContainerAllocator& _alloc)
    : x_dist(0.0)
    , y_dist(0.0)  {
  (void)_alloc;
    }



   typedef double _x_dist_type;
  _x_dist_type x_dist;

   typedef double _y_dist_type;
  _y_dist_type y_dist;





  typedef boost::shared_ptr< ::experiments::exampleRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::experiments::exampleRequest_<ContainerAllocator> const> ConstPtr;

}; // struct exampleRequest_

typedef ::experiments::exampleRequest_<std::allocator<void> > exampleRequest;

typedef boost::shared_ptr< ::experiments::exampleRequest > exampleRequestPtr;
typedef boost::shared_ptr< ::experiments::exampleRequest const> exampleRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::experiments::exampleRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::experiments::exampleRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::experiments::exampleRequest_<ContainerAllocator1> & lhs, const ::experiments::exampleRequest_<ContainerAllocator2> & rhs)
{
  return lhs.x_dist == rhs.x_dist &&
    lhs.y_dist == rhs.y_dist;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::experiments::exampleRequest_<ContainerAllocator1> & lhs, const ::experiments::exampleRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace experiments

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::experiments::exampleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::experiments::exampleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::experiments::exampleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::experiments::exampleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::experiments::exampleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::experiments::exampleRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::experiments::exampleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9e9fe6ad89b5212aaaa506f6cbd26357";
  }

  static const char* value(const ::experiments::exampleRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9e9fe6ad89b5212aULL;
  static const uint64_t static_value2 = 0xaaa506f6cbd26357ULL;
};

template<class ContainerAllocator>
struct DataType< ::experiments::exampleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "experiments/exampleRequest";
  }

  static const char* value(const ::experiments::exampleRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::experiments::exampleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# request\n"
"float64 x_dist\n"
"float64 y_dist\n"
;
  }

  static const char* value(const ::experiments::exampleRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::experiments::exampleRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x_dist);
      stream.next(m.y_dist);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct exampleRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::experiments::exampleRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::experiments::exampleRequest_<ContainerAllocator>& v)
  {
    s << indent << "x_dist: ";
    Printer<double>::stream(s, indent + "  ", v.x_dist);
    s << indent << "y_dist: ";
    Printer<double>::stream(s, indent + "  ", v.y_dist);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EXPERIMENTS_MESSAGE_EXAMPLEREQUEST_H
