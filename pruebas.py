from pyvda import AppView, get_apps_by_z_order, VirtualDesktop, get_virtual_desktops

print("Going to desktop number 2")
print(VirtualDesktop(2).go())

#print("Pinning the current window")
#AppView.current().pin()