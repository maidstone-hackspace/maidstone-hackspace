import os
from scaffold.web import www

class control(www.default.html_ui): 
    """Image cycle widgets"""
    view = []
    buttons = []
    content = []
    count = 0
    with open(os.path.abspath('./widgets/banner_slider.js')) as fp:
        script = [fp.read()]
    
    def create(self):
        self.reset()

    def reset(self):
        self.view = []
        self.buttons = []
        self.content = []

    def append(self, image, link, title, intro=''):
        text = '<div class="content">%s<br />%s</div>' % (title, intro) if title else ''
        if link:
            self.content.append(u'<a href="%s" ><img src="%s" />%s</a>' % (link, image, text))
        else:
            self.content.append(u'<img src="%s" />%s' % (image, text))

    def render(self):
        self.count += 1
        htm = u'<div class="banner-slide" ng-app="myApp" ng-controller="sliderController">'
        htm += u'<ul ng-switch on="currentSlide" ng-init="length=%d;">' % (len(self.content))
        count = 0
        for item in self.content:
            htm += u'<li class="slide" ng-switch-when="%s">%s</li>' % (count, item)
            count += 1
        htm += u'<li style="clear:both;"></li></ul>'
        htm += u'<div ng-click="prev()" title="Previous" role="button" class="slide-button left">&lt;</div>'
        htm += u'<div ng-click="next()" title="Next" role="button" class="slide-button right">&gt;</div>'
        htm += u'</div><div class="clear"></div>'
        return htm
