##import geni.portal as portal
##import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
##request = portal.context.makeRequestRSpec()
# Create a XenVM
##node = request.XenVM("node")
#node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
#node.routable_control_ip = "true"

#node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
#node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y apache2"))
#node.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status apache2'))

# Print the RSpec to the enclosing page.
#portal.context.printRequestRSpec()
import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

pc = portal.Context()
request = pc.makeRequestRSpec()

tourDescription = \
"""
This profile provides the template for a compute node with Docker installed on Ubuntu 18.04
"""

#
# Setup the Tour info with the above description and instructions.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

node = request.XenVM("docker")
node.cores = 4
node.ram = 4096
node.routable_control_ip = "true" 

bs_landing = node.Blockstore("bs_image", "/image")
bs_landing.size = "500GB"
  
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
node.routable_control_ip = "true"
node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/install_docker.sh"))
  
pc.printRequestRSpec(request)
