import React, { PropTypes } from 'react';
import { Card, CardText, CardHeader, CardMedia, CardTitle, GridList } from 'material-ui';

function CardHist(props) {
    let cardsPlayed = props.historyData;
    return (
      <div>
        <p><b>All your Cards played</b></p>
        <div>
            {cardsPlayed &&
                cardsPlayed.map((card, index) => {
                    const imageName = (card.card_name).replace(/\s+/g, '').toLowerCase();
                    let margin = -20;
                    if (index === 1) { margin = 0; }
                    if (index > 0)
                    {
                      return (
                        <Card
                            className="Card"
                            data-card-number={index}
                            key={card.id}
                            style={{
                                margin: `${margin}`,
                                width: 90, display:
                                'inline-block',
                                padding: 0 }}
                        >
                            <CardMedia>
                                <img
                                    alt={`${card.card_name} image`}
                                    src={`dist/images/cards/${imageName}.png`}
                                />
                            </CardMedia>
                        </Card>
                    );
                  }
                })
            }
      </div>
      </div>
    );
}

CardHist.propTypes = {
    historyData: PropTypes.object.isRequired,
};

export default CardHist;
