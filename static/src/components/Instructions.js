import React from 'react';
import { Card, CardText, CardHeader, CardMedia } from 'material-ui';

const Instructions = () => (
    <div className="col-md-8">
        <h1>How to play...</h1>
        <p> Below are some instructions on how to play 7 Wonders</p>
        <p> From original game manual to navigating around our <i>Online Capstone Edition 2017</i> </p>
        <br />
        <Card style={{ width: '100%' }}>
            <CardHeader
                title="Quick Rules and Gameplay"
                actAsExpander={true}
                showExpandableButton={true}
            />
            <CardText expandable={true} style={{ height: 'auto' }}>
                <CardMedia>
                    <embed
                        alt='Rules PDF'
                        src='dist/images/background/QuickRules.pdf#toolbar=0&navpanes=0'
                        style={{ height: '100%' }}
                    />
                </CardMedia>
            </CardText>
        </Card>
        <br />
        <Card style={{ width: '100%' }}>
            <CardHeader
                title="ScreenShots"
                actAsExpander={true}
                showExpandableButton={true}
            />
            <CardText expandable={true} style={{ height: 450 }}>
                <p> Please Note: Proper Screen shots to come. Below is an example </p>
                <CardMedia>
                    <embed
                        alt='Screen Capture - Game Screen'
                        src='dist/images/background/capture.jpg'
                        style={{ height: 400 }}
                    />
                </CardMedia>
            </CardText>
        </Card>
    </div>
);

export default Instructions;
