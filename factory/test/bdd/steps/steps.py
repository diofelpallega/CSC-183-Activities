# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_in
from lettuce import *
from webtest import TestApp
from lettuce import step
from factory.factory import *
import os

@step(u'Given I have the following web resources:')
def given_i_have_the_following_web_resources(step):
        resources = ["www.ubuntu.com","www.redhat.com","www.suse.com","www.maldrake.com"]
        for row in step.hashes:
            web = str(row['web_resources'])
            assert_equal(web in resources, True)
 
@step(u'And I have my "([^"]*)" as my domain')
def and_i_have_my_localhost_as_my_domain(step,domain):
    dom = Domain(domain) 
    assert_equal(domain, dom.getdomain())

@step(u'When I run the tool')
def when_i_run_the_tool(step):
    dom = Domain("localhost") 
    assert_equal("success",dom.run())

@step(u'Then I see the resources:')
def then_i_see_the_resources(step):
    resources = ["www.ubuntu.com","www.redhat.com","www.suse.com","www.maldrake.com"]
    for row in step.hashes:
        web = str(row['web_resources'])
        assert_equal(web in resources, True)

@step(u'Given I freeBsd has this following web resources:')
def given_i_freebsd_has_this_following_web_resources(step):
    assert True, "resources already on the web"

@step(u'Then I see the resources for ftp:')
def then_i_see_the_resources_for_ftp(step):
    dom = Domain("ftp.freebsd.org") 
    assert_equal("success",dom.runftp())


