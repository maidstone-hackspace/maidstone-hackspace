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
        htm = u'<a href="%s" ><img src="%s" /><div class="content">%s<br />%s</div></a>'%(link,image,title,intro)
        self.content.append(htm)

    def render(self):   
        #~ self.script.append(self.javascript())
        self.count+=1
        htm = u'<div class="banner-slide" ng-app="myApp" ng-controller="sliderController">'
        htm += u'<ul style="%s" ng-switch on="currentSlide" ng-init="length=%d;">' % (self.height, len(self.content))
        count = 0
        for item in self.content:
            htm += u'<li class="slide" ng-switch-when="%s">%s</li>' % (count, item)
            count += 1
        #htm += '''<li class="slide" ng-repeat="slide in slides" ng-hide="!isCurrentSlideIndex($index)" ng-show="isCurrentSlideIndex($index)"><a href="{{slide.link}}" ><img src="{{slide.src}}" /><div class="content">{{slide.title}}<br />{{slide.description}}</div></a></li>'''
        htm += u'<li style="clear:both;"></li></ul>'
        htm += u'<div ng-click="prev()" title="Previous" role="button" class="slide-button left">&lt;</div>'
        htm += u'<div ng-click="next()" title="Next" role="button" class="slide-button right">&gt;</div>'
        htm += u'</div><div class="clear"></div>'
        return htm
