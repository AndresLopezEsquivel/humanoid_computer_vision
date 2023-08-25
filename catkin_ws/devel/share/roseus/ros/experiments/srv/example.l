;; Auto-generated. Do not edit!


(when (boundp 'experiments::example)
  (if (not (find-package "EXPERIMENTS"))
    (make-package "EXPERIMENTS"))
  (shadow 'example (find-package "EXPERIMENTS")))
(unless (find-package "EXPERIMENTS::EXAMPLE")
  (make-package "EXPERIMENTS::EXAMPLE"))
(unless (find-package "EXPERIMENTS::EXAMPLEREQUEST")
  (make-package "EXPERIMENTS::EXAMPLEREQUEST"))
(unless (find-package "EXPERIMENTS::EXAMPLERESPONSE")
  (make-package "EXPERIMENTS::EXAMPLERESPONSE"))

(in-package "ROS")





(defclass experiments::exampleRequest
  :super ros::object
  :slots (_x_dist _y_dist ))

(defmethod experiments::exampleRequest
  (:init
   (&key
    ((:x_dist __x_dist) 0.0)
    ((:y_dist __y_dist) 0.0)
    )
   (send-super :init)
   (setq _x_dist (float __x_dist))
   (setq _y_dist (float __y_dist))
   self)
  (:x_dist
   (&optional __x_dist)
   (if __x_dist (setq _x_dist __x_dist)) _x_dist)
  (:y_dist
   (&optional __y_dist)
   (if __y_dist (setq _y_dist __y_dist)) _y_dist)
  (:serialization-length
   ()
   (+
    ;; float64 _x_dist
    8
    ;; float64 _y_dist
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x_dist
       (sys::poke _x_dist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_dist
       (sys::poke _y_dist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x_dist
     (setq _x_dist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_dist
     (setq _y_dist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass experiments::exampleResponse
  :super ros::object
  :slots (_x_undis _y_undis ))

(defmethod experiments::exampleResponse
  (:init
   (&key
    ((:x_undis __x_undis) 0.0)
    ((:y_undis __y_undis) 0.0)
    )
   (send-super :init)
   (setq _x_undis (float __x_undis))
   (setq _y_undis (float __y_undis))
   self)
  (:x_undis
   (&optional __x_undis)
   (if __x_undis (setq _x_undis __x_undis)) _x_undis)
  (:y_undis
   (&optional __y_undis)
   (if __y_undis (setq _y_undis __y_undis)) _y_undis)
  (:serialization-length
   ()
   (+
    ;; float64 _x_undis
    8
    ;; float64 _y_undis
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x_undis
       (sys::poke _x_undis (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_undis
       (sys::poke _y_undis (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x_undis
     (setq _x_undis (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_undis
     (setq _y_undis (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass experiments::example
  :super ros::object
  :slots ())

(setf (get experiments::example :md5sum-) "76b5930aa6e27a49039927b2ca52db98")
(setf (get experiments::example :datatype-) "experiments/example")
(setf (get experiments::example :request) experiments::exampleRequest)
(setf (get experiments::example :response) experiments::exampleResponse)

(defmethod experiments::exampleRequest
  (:response () (instance experiments::exampleResponse :init)))

(setf (get experiments::exampleRequest :md5sum-) "76b5930aa6e27a49039927b2ca52db98")
(setf (get experiments::exampleRequest :datatype-) "experiments/exampleRequest")
(setf (get experiments::exampleRequest :definition-)
      "# request
float64 x_dist
float64 y_dist
---
# result
float64 x_undis
float64 y_undis
")

(setf (get experiments::exampleResponse :md5sum-) "76b5930aa6e27a49039927b2ca52db98")
(setf (get experiments::exampleResponse :datatype-) "experiments/exampleResponse")
(setf (get experiments::exampleResponse :definition-)
      "# request
float64 x_dist
float64 y_dist
---
# result
float64 x_undis
float64 y_undis
")



(provide :experiments/example "76b5930aa6e27a49039927b2ca52db98")


