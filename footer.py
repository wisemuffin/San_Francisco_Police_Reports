import dash_html_components as html

# set up footer
theme = {
    # 'font-family': 'Raleway',
    'background-color': '#ddd',
}


def create_footer():
    # p = html.P(
    #     children=[
    #         html.Span('Built with '),
    #         html.A('Plotly Dash',
    #                href='https://github.com/plotly/dash', target='_blank'),
    #         # html.Span(' and:'),
    #     ],
    #     style = {
    #         'display': 'inline-block',
    #         'width': '80%',
    #         # 'display': 'flex',
    #         'justify-content': 'left',
    #         'align-items':'left',
    #         'height':'2em',
    #         'margin': '0',
    #         'padding': '0.5em'
    #     }
    # )

    hashtags = 'plotly,dash,nhs'
    tweet = 'Dash UK NHS, a cool dashboard with Plotly Dash!'
    twitter_href = 'https://twitter.com/intent/tweet?hashtags={}&text={}'\
        .format(hashtags, tweet)

    twitter = html.A(
        children=html.I(children=[], className='fa fa-twitter fa-3x'),
        title='Tweet me!', href=twitter_href, target='_blank')

    linkedin = html.A(
        children=html.I(children=[], className='fa fa-linkedin-square fa-3x'),
        title='My Linkedin',
        href='https://www.linkedin.com/in/david-griffiths-5a9387a1/', target='_blank')

    github = html.A(
        children=html.I(children=[], className='fa fa-github fa-3x'),
        title='Repo on GitHub',
        href='https://github.com/wisemuffin/CS50project', target='_blank')

    li_right_first = {'line-style-type': 'none', 'display': 'inline-block'}
    li_right_others = {k: v for k, v in li_right_first.items()}
    li_right_others.update({'margin-left': '10px'})
    ul = html.Ul(
        children=[
            html.Li(twitter, style=li_right_first),
            html.Li(linkedin, style=li_right_others),
            html.Li(github, style=li_right_others),
        ],
        style={
            # 'width':'20%',
            # 'display': 'inline-block',
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'height': '70%',
            'margin': '0',
            'padding': '0.5em'
        }

    )

    div = html.Div([ul])  # div = html.Div([p, ul])
    footer_style = {
        'font-size': '1.2em',
        'background-color': theme['background-color'],
        'padding': '1rem',  # '0.5em',
        #'width': '100%',
        'bottom': '0',
        'right': '0',
        'left': '0',
        'text-align': 'centre',
        'position': 'absolute'
    }
    footer = html.Footer(div, style=footer_style)
    return footer
