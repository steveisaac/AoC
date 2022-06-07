import numpy

scanners = []

transforms = []

## rotate around x axis
x_rot = numpy.array([[1,0,0],[0,0,-1],[0,1,0]])
## rotate around y axis
y_rot = numpy.array([[0,0,1],[0,1,0],[-1,0,0]])
## rotate around z axis
z_rot = numpy.array([[0,1,0],[-1,0,0],[0,0,1]])
identity = numpy.identity(3, int)
transforms = []
for direction in [identity, y_rot, y_rot.dot(y_rot), y_rot.dot(y_rot).dot(y_rot), z_rot, z_rot.dot(z_rot).dot(z_rot)]:
        for orientation in [identity, x_rot, x_rot.dot(x_rot), x_rot.dot(x_rot).dot(x_rot)]:
                transforms.append(direction.dot(orientation))

# try scaling all els in a view by setting to an el from another box then scale

with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day19.txt") as puzzle_input:
    for line in puzzle_input:
        if line[0:2] == '--':
            scanners.append([])
        elif line.strip():
            scanners[-1].append([int(i)for i in line.strip().split(",")])

point_map = set()

scanners = map(numpy.array, scanners)
# Initially populate with first scanner
scanners_to_check = [next(scanners)]
oriented_beacons = {tuple(beacon) for beacon in scanners_to_check[0]}
unoriented_scanners = list(scanners)
scanner_locations = [numpy.zeros(3, int)]

##while len(scanners_to_check) > 0:
for scanner in scanners_to_check:
        scanner_set = {tuple(b) for b in scanner}
        i = 0
        while i < len(unoriented_scanners):
                # We need to check candidate in all 24 orientations
                matched = False
                for t in transforms:
                        if matched == True:
                                break
                        reoriented_candidate = unoriented_scanners[i].dot(t)
                        # dont bother checking last 11 beacons as they'll never have 12+ shared beacons
                        for cb in reoriented_candidate[:-11]:
                                if matched == True:
                                        break
                                for sb in scanner:
                                        if matched == True:
                                                break
                                        moved_candidate = reoriented_candidate - (cb - sb)
                                        mc_set = {tuple(b) for b in moved_candidate}
                                        shared_beacons = mc_set & scanner_set
                                        if len(shared_beacons) >= 12:
                                                scanners_to_check.append(moved_candidate)
                                                oriented_beacons |= mc_set
                                                unoriented_scanners.pop(i)
                                                i -= 1
                                                scanner_locations.append(sb-cb)
                                                matched = True
                i += 1

m = [sum(abs(scanner_locations[i] - scanner_locations[j])) for i in range(len(scanner_locations)-1) for j in range(i+1, len(scanner_locations))]
print(max(m))
                
