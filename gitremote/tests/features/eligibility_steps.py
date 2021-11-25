from pytest_bdd import scenario, given, when, then


@given("application is requesting year of birth")
def step_impl():
    raise NotImplementedError(u'STEP: Given application is requesting year of birth')


@when("the user presses Enter")
def step_impl():
    raise NotImplementedError(u'STEP: When the user presses Enter')


@then("application closes")
def step_impl():
    raise NotImplementedError(u'STEP: Then application closes')