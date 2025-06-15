



import { Grid, Paper, Typography } from '@mui/material';



interface Stat{
    label: string;
    value: string | number;
}

interface BasicInfoMatchProps {
    stats: Stat[];
  }


const BasicInfoMatch = ({ stats }: BasicInfoMatchProps) => {

    return (
    <Paper
      elevation={4}
      sx={{
        backgroundColor: 'rgba(255, 255, 255, 0.95)',
        borderRadius: 3,
        padding: 3,
        margin: 2,
        
      }}
    >
      <Grid container spacing={2}>
        {stats.map((item, index) => (
          <Grid size={{ xs:12, sm:6, md:4 }} key={index}>
            <Paper
              elevation={2}
              sx={{
                padding: 2,
                borderRadius: 2,
                height: '100%',
                backgroundColor: 'grey.100',
              }}
            >
              <Typography
                variant="subtitle2"
                sx={{ fontWeight: 'bold', color: 'text.secondary', mb: 1 }}
              >
                {item.label}
              </Typography>
              <Typography variant="body1" color="text.primary" sx={{ fontWeight: 'bold' }}>
                {item.value}
              </Typography>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Paper>
  );


}

export default BasicInfoMatch;