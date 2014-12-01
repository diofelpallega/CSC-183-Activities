from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp 
from nose.tools import assert_equal, assert_in
from crawler.crawler import * 
import os.path


@step(u'Given I input site "([^"]*)"')
def given_i_input_site_group1(step, site):
    a = GetSite(site)
    whatsite = a.site 
    assert_equal(site, whatsite)

@step(u'When I get image "([^"]*)" from "([^"]*)"')
def then_i_get_image_group1(step, imagelink, source):
    site = GetSite(source)
    imagesite = site.getimagesource(source)
    assert_equal(imagelink, imagesite)


@step(u'Then "([^"]*)" from "([^"]*)" is in "([^"]*)"')
def then_group1_from_group2_is_in_group3(step, thefile, source,directory):
    filedirectory = directory + "/" +thefile 
    wherefile = os.path.realpath(thefile)
    assert_equal(True,os.path.isfile(directory+thefile))
