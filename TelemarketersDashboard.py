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
                           color_continuous_scale='greens',  # Consider if this color scheme is the most appropriate
                           title='Top 10 Telemarketers by Average Calls per Day')

fig_avg_calls.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),  # Adjust margins to ensure no cutoffs
    coloraxis_colorbar=dict(
        title="Avg Calls per Day",
        thickness=20,
        len=0.5,
        yanchor="top",
        y=0.5
    ),
    font=dict(size=12)  # Adjust font size for better readability
)

fig_avg_calls.update_traces(
    textinfo="label+value+percent parent",  # Show more info on hover
    hovertemplate="<b>%{label}</b><br>Average Calls: %{value}<br>Percentage: %{percent parent}<extra></extra>"
)


# Conversion Rate
fig_conversion = px.treemap(top_conversion,
                            path=[px.Constant("Top 10 Telemarketers"), 'Name'],
                            values='Conversion Rate',
                            color='Conversion Rate',
                            color_continuous_scale='greens',
                            title='Top 10 Telemarketers by Conversion Rate')
fig_conversion.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),  # Adjust margins to ensure no cutoffs
    coloraxis_colorbar=dict(
        title="Conversion Rate",
        thickness=20,
        len=0.5,
        yanchor="top",
        y=0.5
    ),
    font=dict(size=12)  # Adjust font size for better readability
)
fig_conversion.update_traces(
    textinfo="label+value+percent parent",  # Show more info on hover
    hovertemplate="<b>%{label}</b><br>Conversion Rate: %{value}<br>Percentage: %{percent parent}<extra></extra>"
)



# Engagement with Decision Makers
fig_engagement = px.treemap(top_engagement,
                            path=[px.Constant("Top 10 Telemarketers"), 'Name'],
                            values='Engagement with Decision Makers',
                            color='Engagement with Decision Makers',
                            color_continuous_scale='greens',
                            title='Top 10 Telemarketers by Engagement with Decision Makers')
fig_engagement.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),  # Adjust margins to ensure no cutoffs
    coloraxis_colorbar=dict(
        title="Engagement with Decision Makers",
        thickness=20,
        len=0.5,
        yanchor="top",
        y=0.5
    ),
    font=dict(size=12)  # Adjust font size for better readability
)
fig_engagement.update_traces(
    textinfo="label+value+percent parent",  # Show more info on hover
    hovertemplate="<b>%{label}</b><br>Engagement with Decision Makers: %{value}<br>Percentage: %{percent parent}<extra></extra>"
)    


# Data preparation for the line chart of Total Daily Calls
daily_calls_columns = ['Calls 10/25', 'Calls 10/26', 'Calls 10/27', 'Calls 10/30', 'Calls 10/31']
daily_totals = df[daily_calls_columns].sum()

# Assuming 'df' is your DataFrame and 'daily_totals' is calculated as shown
daily_totals_df = pd.DataFrame({
    'Date': ['10/25', '10/26', '10/27', '10/30', '10/31'],
    'Total Calls': daily_totals.values
})

# Assuming daily_totals_df is your DataFrame and is already defined
fig_line = px.line(daily_totals_df, x='Date', y='Total Calls', markers=True,
                   title='Daily Calls 10/25 - 10/31',
                   color_discrete_sequence=["#007bff"])  # A more vibrant color

# Update layout for better visual appeal
fig_line.update_layout(
    xaxis_title='Date',
    yaxis_title='Total Calls',
    showlegend=False,
    title_font=dict(size=22, color='darkblue', family='Arial, sans-serif'),
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    plot_bgcolor='white',  # Set background color to white for a cleaner look
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins to prevent cut-offs
    hovermode='x unified'  # Improve hover info
)

# Optionally, increase line width and customize marker appearance
fig_line.update_traces(line=dict(width=3), marker=dict(size=10, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')))

# Assuming 'df' and necessary libraries (pandas, plotly.express) are already imported

# Name shortening improved for edge cases
df['Name'] = df['Name'].apply(lambda x: ". ".join([y[0] if i == 0 else y for i, y in enumerate(x.split())]))

# Data preparation remains the same
scatter_data = df[['Name', 'Performance Metric', 'Difference']]

# Improved scatter plot plotting
fig_scatter = px.scatter(scatter_data, x='Performance Metric', y='Difference',
                         color='Difference', # Color coding by 'Difference' or another variable could add depth
                         color_continuous_scale=px.colors.diverging.Tealrose, # Using a diverging color scale for visual appeal
                         title='Performance vs. Supervisor Rating',
                         hover_name='Name') # Adding hover information

# Adding a more visible horizontal line
fig_scatter.add_hline(y=0, line_dash="dot", line_color="blue", line_width=2)

# Modifying annotations for better visibility and avoiding overlap where possible
fig_scatter.add_annotation(x=0.1, y=0.9, text="Overrated", showarrow=False, 
                           xref="paper", yref="paper", font_color="red", bgcolor="white")
fig_scatter.add_annotation(x=0.9, y=0.1, text="Underrated", showarrow=False, 
                           xref="paper", yref="paper", font_color="green", bgcolor="white")

# Dynamically added annotations are omitted for clarity

fig_scatter.update_layout(xaxis_title='Real Performance',
                          yaxis_title='Supervisory Over/Underestimation',
                          legend_title_text='Rating Difference') # If using color coding


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
