
import pymel.core as pm

NAMESPACE = 'LOOKDEV'


def create():
    '''
    Creates three spheres (white, 50% grey and chrome ball) and a colorchecker/Macbeth chart
    Args:
        name(String): Name of the object
    Returns:
        colorchecker
    '''
    white_ball = create_lightchecker(name='white')
    grey_ball = create_lightchecker(name='grey')
    chrome_ball = create_lightchecker(name='chrome')
    colorchecker = create_colorchecker(name='colorchart')
    colorcheckers_grp = pm.group(white_ball, grey_ball, chrome_ball, colorchart,
                                 name='%s:colorcheckers_grp' % NAMESPACE)

    white_ball.translate.set(0, 20, 0)
    grey_ball.translate.set(-7.5, 7, 0)
    chrome_ball.translate.set(7.5, 7, 0)
    colorchart.translate.set(0, -13.65, 0)


def create_colorchecker(name):
    '''
    Creates three spheres (white, 50% grey and chrome ball) and a colorchecker/Macbeth chart
    Args:
        name(String): Name of the object
    Returns:
        colorchecker
    '''

    colorchart = pm.polyPlane(name='%s:colorchart_geo' % NAMESPACE,
                              width=35.83, height=25.25, axis=(0, 0, 1),
                              constructionHistory=False)[0]
    return colorchart


def create_lightchecker(name):
    '''
    Creates a poly mesh to use as lightchecker.
    Args:
        name(String): Name of the object
    Returns:
        lightchecker
    '''
    lightchecker = pm.polySphere(name='{0}:{1}_geo'.format(NAMESPACE, name), radius=7,
                                 subdivisionsX=60, subdivisionsY=40,
                                 constructionHistory=False)[0]
    return lightchecker


def create_shader(name):
    '''
    Creates a shader to assign to each colorchecker.
    Args:
        name(String): Name of the shader
    Returns:
        Shader
    '''
    pass
