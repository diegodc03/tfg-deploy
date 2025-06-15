
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

import React from 'react';
import CardActionArea from '@mui/material/CardActionArea';
import { useNavigate } from 'react-router-dom';
import { Box } from '@mui/material';
import { getBackgroundColorByLeague, getBackgroundGradientByLeague } from '../model/constants/constants';
import  imgRU  from '../images/flags/inglaterra.png'

type CardShowProps = {
    title: string;
    season?: string; // Prop opcional para la liga
    week?: string; // Prop opcional para la semana
    result?: string; // Prop opcional para el resultado
    navigateElement?: string; // Prop opcional para la navegación   
};

const CardShowOptions: React.FC<CardShowProps> = ({ title, season, week, result, navigateElement }) => {

    const navigate = useNavigate();

    const handleChangeScoresView = () => {
        if (navigateElement) {
            navigate(`${navigateElement}`);   
        }
    };

    const getBackgroundImage = (title: string) => {
        if (title === 'Premier League') {
            return `url(${imgRU})`; // URL de la imagen para La Liga
        }
    }


    return (
        <Card
            sx={{
                width: 220,
                minHeight: 160,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                borderRadius: 3,
                position: 'relative',
                paddingBottom: 1,
                background  : getBackgroundGradientByLeague(title), 
                backgroundImage: getBackgroundImage(title), 
                backgroundSize: 'cover',
                backgroundPosition: 'center',
            }}
        >          
           <CardActionArea onClick={handleChangeScoresView}>
                <CardContent
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        backgroundColor: '#f5f5f5',  // color neutro claro
                        borderRadius: 2,
                        padding: 2,
                        marginLeft: '10px',
                        marginRight: '33px',
                        boxShadow: '0px 10px 15px rgba(0, 0, 0, 0.6)',  // sombra suave
                        marginTop: 1,   // un pequeño margen arriba
                    }}
                    >
                    <Typography gutterBottom variant="h6" component="div" fontWeight="bold" >
                        {title}
                    </Typography>
                    <Box>
                        <Typography variant="h6" fontWeight="bold">
                        {season && <>{season}<br /></>}
                        </Typography>
                        <Typography variant="body1">
                        {week && <><strong>Semana:</strong> {week}<br /></>}
                        {result && <><strong>Resultado:</strong> {result}</>}
                        </Typography>
                    </Box>
                </CardContent>

          </CardActionArea>
        </Card>
      );
  };

export default CardShowOptions;