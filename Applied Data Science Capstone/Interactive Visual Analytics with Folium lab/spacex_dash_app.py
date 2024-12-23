{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Connected to Python 3.12.4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81e38e1f-40f2-4fa8-848f-156d5edc7f2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-1-80399ae46a67>:4: UserWarning: \n",
      "The dash_html_components package is deprecated. Please replace\n",
      "`import dash_html_components as html` with `from dash import html`\n",
      "  import dash_html_components as html\n",
      "<ipython-input-1-80399ae46a67>:5: UserWarning: \n",
      "The dash_core_components package is deprecated. Please replace\n",
      "`import dash_core_components as dcc` with `from dash import dcc`\n",
      "  import dash_core_components as dcc\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x131a3dbd760>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import dash\n",
    "import dash_html_components as html\n",
    "import dash_core_components as dcc\n",
    "from dash.dependencies import Input, Output\n",
    "import plotly.express as px\n",
    "\n",
    "# Read the airline data into pandas dataframe\n",
    "spacex_df = pd.read_csv(\"spacex_launch_dash.csv\")\n",
    "max_payload = spacex_df['Payload Mass (kg)'].max()\n",
    "min_payload = spacex_df['Payload Mass (kg)'].min()\n",
    "\n",
    "# Create a dash application\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "# Create an app layout\n",
    "app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',\n",
    "                                        style={'textAlign': 'center', 'color': '#503D36',\n",
    "                                               'font-size': 40}),\n",
    "                                # TASK 1: Add a dropdown list to enable Launch Site selection\n",
    "                                # The default select value is for ALL sites\n",
    "                                # dcc.Dropdown(id='site-dropdown',...)\n",
    "                                dcc.Dropdown(id='site-dropdown',\n",
    "                                             options=[\n",
    "                                                     {'label': 'All Sites', 'value': 'ALL'},\n",
    "                                                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},\n",
    "                                                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},\n",
    "                                                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},\n",
    "                                                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}\n",
    "                                                     ],\n",
    "                                             value='ALL',\n",
    "                                             placeholder='Select a Launch Site here',\n",
    "                                             searchable=True\n",
    "                                             # style={'width':'80%','padding':'3px','font-size':'20px','text-align-last':'center'}\n",
    "                                             ),\n",
    "                                html.Br(),\n",
    "\n",
    "                                # TASK 2: Add a pie chart to show the total successful launches count for all sites\n",
    "                                # If a specific launch site was selected, show the Success vs. Failed counts for the site\n",
    "                                html.Div(dcc.Graph(id='success-pie-chart')),\n",
    "                                html.Br(),\n",
    "\n",
    "                                html.P(\"Payload range (Kg):\"),\n",
    "                                # TASK 3: Add a slider to select payload range\n",
    "                                #dcc.RangeSlider(id='payload-slider',...)\n",
    "                                dcc.RangeSlider(id='payload-slider',\n",
    "                                                min=0,\n",
    "                                                max=10000,\n",
    "                                                step=1000,\n",
    "                                                value=[min_payload, max_payload]\n",
    "                                                ),\n",
    "\n",
    "                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success\n",
    "                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),\n",
    "                                ])\n",
    "\n",
    "# TASK 2:\n",
    "# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output\n",
    "@app.callback(Output(component_id='success-pie-chart', component_property='figure'),\n",
    "              Input(component_id='site-dropdown', component_property='value'))\n",
    "def get_pie_chart(entered_site):\n",
    "    filtered_df = spacex_df\n",
    "    if entered_site == 'ALL':\n",
    "        fig = px.pie(filtered_df, values='class', \n",
    "        names='Launch Site', \n",
    "        title='Success Count for all launch sites')\n",
    "        return fig\n",
    "    else:\n",
    "        # return the outcomes piechart for a selected site\n",
    "        filtered_df=spacex_df[spacex_df['Launch Site']== entered_site]\n",
    "        filtered_df=filtered_df.groupby(['Launch Site','class']).size().reset_index(name='class count')\n",
    "        fig=px.pie(filtered_df,values='class count',names='class',title=f\"Total Success Launches for site {entered_site}\")\n",
    "        return fig\n",
    "\n",
    "# TASK 4:\n",
    "# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output\n",
    "@app.callback(Output(component_id='success-payload-scatter-chart',component_property='figure'),\n",
    "                [Input(component_id='site-dropdown',component_property='value'),\n",
    "                Input(component_id='payload-slider',component_property='value')])\n",
    "def scatter(entered_site,payload):\n",
    "    filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(payload[0],payload[1])]\n",
    "    # thought reusing filtered_df may cause issues, but tried it out of curiosity and it seems to be working fine\n",
    "    \n",
    "    if entered_site=='ALL':\n",
    "        fig=px.scatter(filtered_df,x='Payload Mass (kg)',y='class',color='Booster Version Category',title='Success count on Payload mass for all sites')\n",
    "        return fig\n",
    "    else:\n",
    "        fig=px.scatter(filtered_df[filtered_df['Launch Site']==entered_site],x='Payload Mass (kg)',y='class',color='Booster Version Category',title=f\"Success count on Payload mass for site {entered_site}\")\n",
    "        return fig\n",
    "\n",
    "# Run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
