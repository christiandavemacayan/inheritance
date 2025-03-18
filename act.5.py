class CreativeEntrepreneur:
    def __init__(self, name):
        self.name = name

class RawDesigner(CreativeEntrepreneur):
    def __init__(self, name):
        super().__init__(name)

    def createDesign(self):
        print(f"{self.name} is creating a raw design for a project.")

class ContentStrategist(CreativeEntrepreneur):
    def __init__(self, name):
        super().__init__(name)

    def planContent(self):
        print(f"{self.name} is planning content strategy for the brand.")

class TalesFromTheIslandsCreator(RawDesigner, ContentStrategist):
    def __init__(self, name, trending_topic):
        RawDesigner.__init__(self, name)
        ContentStrategist.__init__(self, name)
        self.trending_topic = trending_topic

    def produceReel(self):
        if self.trending_topic.lower() == "conspiracy theories":
            print(f"{self.name} is producing a reel focusing on conspiracy theories.")
        elif self.trending_topic.lower() == "motivational stories":
            print(f"{self.name} is producing a reel focusing on motivational stories.")
        else:
            print(f"{self.name} is producing a reel on a different topic: {self.trending_topic}.")

# Example usage
if __name__ == "__main__":
    creator_name = "Jordan"
    trending_topic = "motivational stories"
    
    creator = TalesFromTheIslandsCreator(creator_name, trending_topic)
    creator.createDesign()
    creator.planContent()
    creator.produceReel()