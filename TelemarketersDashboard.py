import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df =  pd.read_excel("C:\\Users\\Carleano Libretto\\Downloads\\2023 Dataset Telemarketeers.xlsx")
# Data preparation for the treemap of Average Calls per Day
top_average_calls = df.nlargest(10, 'Average Calls per Day')
top_conversion = df.nlargest(10, 'Conversion Rate')
top_engagement = df.nlargest(10, 'Engagement with Decision Makers')
# Theme application


# Avg Calls per day

fig_avg_calls = px.treemap(top_average_calls,
                           path=[px.Constant("Top 10 Telemarketers"), 'Name'],
                           values='Average Calls per Day',
                           color='Average Calls per Day',
                           color_continuous_scale='Reds',
                           title='Top 10 Telemarketers by Average Calls per Day')
fig_avg_calls.update_layout(coloraxis_colorbar=dict(title="Avg Calls per Day"))


# Conversion Rate
fig_conversion = px.treemap(top_conversion,
                            path=[px.Constant("Top 10 Telemarketers"), 'Name'],
                            values='Conversion Rate',
                            color='Conversion Rate',
                            color_continuous_scale='Reds',
                            title='Top 10 Telemarketers by Conversion Rate')
fig_conversion.update_layout(coloraxis_colorbar=dict(title="Conversion Rate"))


# Engagement with Decision Makers
fig_engagement = px.treemap(top_engagement,
                            path=[px.Constant("Top 10 Telemarketers"), 'Name'],
                            values='Engagement with Decision Makers',
                            color='Engagement with Decision Makers',
                            color_continuous_scale='Reds',
                            title='Top 10 Telemarketers by Engagement with Decision Makers')
fig_engagement.update_layout(coloraxis_colorbar=dict(title="Engagement with Decision Makers"))


# Data preparation for the line chart of Total Daily Calls
daily_calls_columns = ['Calls 10/25', 'Calls 10/26', 'Calls 10/27', 'Calls 10/30', 'Calls 10/31']
daily_totals = df[daily_calls_columns].sum()

# Assuming 'df' is your DataFrame and 'daily_totals' is calculated as shown
daily_totals_df = pd.DataFrame({
    'Date': ['10/25', '10/26', '10/27', '10/30', '10/31'],
    'Total Calls': daily_totals.values
})

fig_line = px.line(daily_totals_df, x='Date', y='Total Calls', markers=True,
                   title='Daily Calls 10/25 - 10/31',
                   color_discrete_sequence=["black"])
fig_line.update_layout(xaxis_title='Date', yaxis_title='Total Calls', showlegend=False)

#make a list of names for the scatter plots where it is F. Name to save space and make it more readable
df['Name'] = df['Name'].apply(lambda x: x.split()[0][0] + '. ' + x.split()[1])

# Data preparation for the scatterplot
scatter_data = df[['Name', 'Performance Metric', 'Difference']]
# Scatterplot plotting
# Assuming 'scatter_data' is prepared as shown
fig_scatter = px.scatter(scatter_data, x='Performance Metric', y='Difference', color_discrete_sequence=["black"],
                         title='Performance vs. Supervisor Rating')
fig_scatter.add_hline(y=0, line_dash="dot", line_color="red",)
fig_scatter.add_annotation(x=0.1, y=0.9, text="Overrated", showarrow=False, xref="paper", yref="paper", font_color="green",  bordercolor="green", borderwidth=1)
fig_scatter.add_annotation(x=0.9, y=0.1, text="Underrated", showarrow=False, xref="paper", yref="paper", font_color="red",  bordercolor="red", borderwidth=1)
# Adding annotations for each point
for i, row in scatter_data.iterrows():
    fig_scatter.add_annotation(x=row['Performance Metric'], y=row['Difference'], text=row['Name'],
                               showarrow=True, arrowhead=1, ax=0, ay=-40)

fig_scatter.update_layout(xaxis_title='Real Performance', yaxis_title='Difference')

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
    html.H1('Telemarketer Performance Dashboard', style={'text-align': 'center'}),
    html.Div([
        dcc.Graph(id='avg-calls-per-day', figure=fig_avg_calls),
        dcc.Graph(id='conversion-rate', figure=fig_conversion),
        dcc.Graph(id='engagement', figure=fig_engagement)
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),
    html.Div([
        dcc.Graph(id='total-daily-calls', figure=fig_line),
        dcc.Graph(id='performance-scatter', figure=fig_scatter)
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'})
], style={'max-width': '1200px', 'margin': '0 auto'})

if __name__ == '__main__':
    app.run_server(debug=True)
