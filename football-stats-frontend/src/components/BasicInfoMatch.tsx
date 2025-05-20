



import { Grid, Typography } from '@mui/material';



interface Stat{
    label: string;
    value: string | number;
}

interface BasicInfoMatchProps {
    stats: Stat[];
  }


const BasicInfoMatch = ({ stats }: BasicInfoMatchProps) => {

    return (
        <>
            
        <Grid 
            container 
            justifyContent="center" 
            alignItems="center" 
            sx={{
                backgroundColor: 'rgba(255, 255, 255, 0.9)', 
                paddingTop: 3, 
                borderRadius: 2 
            }}
        >

            <Grid 
                container 
                spacing={2} 
                justifyContent={"left"} 
                sx={{ 
                    marginLeft: 2 
                    }}
            >
                {stats.map((item, index) => (
                    <Grid size = {{ xs:6, sm:6, md:4}} key={index} >    
                        <Typography variant="h6" gutterBottom sx={{ fontWeight: 'bold' }}>
                            {item.label}:
                        </Typography>
                        <Typography variant="body1" gutterBottom sx={{ marginBottom: 1 }}>
                            {item.value}
                        </Typography> 
                    </Grid>   
                ))};

            </Grid>                
        </Grid>
        
        
        </>

    );


}

export default BasicInfoMatch;