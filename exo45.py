class Scene(object):

        def enter(self):
                print ""
                exit(1)
                
class Engine(object): #holder styr på nivåene
        
        def __init__(self, scene_map):
                self.scene_map = scene_map
                
        def play(self): #spillet starter på nivå 1
                current_scene = self.scene_map.opening_scene()
                
                while True:
                        print "\n--------"
                        next_scene_name = current_scene.enter()
                        current_scene = self.scene_map.next_scene(next_scene_name)
                        
class Dead(Scene): # Du taper spillet

        quips = [
                "Du tapte"
        ]
                
        def enter(self):
                print Dead.quips[randint(0, len(self.quips)-1)]
                exit(1)
