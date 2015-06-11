import os
from scaffold.web import www

class control(www.default.html_ui): 
    """Image cycle widgets"""
    view=[]
    buttons=[]
    content=[]
    count=0
    offset=60
    height=300
    width=400
    
    with open(os.path.abspath('./widgets/banner_slider.js')) as fp:
        script = [fp.read()]
    
    #~ def javascript(self):
        #~ return fp.read()
        #~ self.script.append()
    
    def create(self):
        self.reset()

    def reset(self):
        self.view=[]
        self.buttons=[]
        self.content=[]

    def append(self,image,link,title,intro=''):
        htm='<a href="%s" ><img src="%s" /><div class="content">%s<br />%s</div></a>'%(link,image,title,intro)
        self.content.append(htm)

    def render(self):   
        #~ self.script.append(self.javascript())
        self.count+=1
        htm='<div class="banner-slide" ng-app="myApp" ng-controller="sliderController">'
        htm+='<ul style="%s" >' % self.height
        count=0
        #~ for item in self.content:
            #~ htm+='<li class="slide" ng-hide="!isCurrentSlideIndex($index)">%s</li>' % (item)
            #~ count+=1
        htm += '''<li class="slide" ng-repeat="slide in slides" ng-hide="!isCurrentSlideIndex($index)" ng-show="isCurrentSlideIndex($index)"><a href="{{slide.link}}" ><img src="{{slide.src}}" /><div class="content">{{slide.title}}<br />{{slide.description}}</div></a></li>'''
        htm += '<li style="clear:both;"></li></ul>'
        htm += '<div ng-click="prev()" title="Previous" class="left">&lt;</div><div ng-click="next()" title="Next" class="right">&gt;</div>'
        htm += '</div><div class="clear"></div>'
        return htm
