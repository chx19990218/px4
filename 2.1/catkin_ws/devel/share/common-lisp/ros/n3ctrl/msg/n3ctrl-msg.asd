
(cl:in-package :asdf)

(defsystem "n3ctrl-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ControllerDebug" :depends-on ("_package_ControllerDebug"))
    (:file "_package_ControllerDebug" :depends-on ("_package"))
  ))